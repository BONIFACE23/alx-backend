import express from 'express';
import redis from 'redis';
import { promisify } from 'util';

const listProducts = [
  {itemId: 1, itemName: 'Suitcase 250', price: 50, initialAvailableQuantity: 4},
  {itemId: 2, itemName: 'Suitcase 450', price: 100, initialAvailableQuantity: 10},
  {itemId: 3, itemName: 'Suitcase 650', price: 350, initialAvailableQuantity: 2},
  {itemId: 4, itemName: 'Suitcase 1050', price: 550, initialAvailableQuantity: 5},
];

const getItemById = (id) => {
  return listProducts.find(item => item.itemId === id);
};

const app = express()

app.get('/list_products', (_req, res) => {
  res.json(listProducts);
});

const client = redis.createClient()

const reserveStockById = (itemId, stock) => {
  client.set(itemId, stock, (err, reply) => {
  if (err) {
      console.error('Error setting value:', err);
    } else {
      redis.print(reply);
    }
  });
};

const getCurrentReservedStockById = async (itemId) => {
  const getVal = promisify(client.get).bind(client);
  const reply = await getVal(itemId);
  return reply;
};

app.get('/list_products/:itemId(\\d+)', (req, res) => {
  const itemId = Number.parseInt(req.params.itemId);
  const productItem = getItemById(itemId);
  
  if (!productItem) {
    res.json({ status: 'Product not found' });
    return;
  }
  
  getCurrentReservedStockById(itemId)
    .then((result) => Number.parseInt(result || 0))
    .then((reservedStock) => {
      productItem.currentQuantity = productItem.initialAvailableQuantity - reservedStock;
      res.json(productItem);
  });
});

app.get('/reserve_product/:itemId(\\d+)', async (req, res) => {
  const itemId = Number.parseInt(req.params.itemId);
  const productItem = getItemById(itemId);
  
  if (!productItem) {
    res.json({ status: 'Product not found' });
    return;
  }
  
  const result = await getCurrentReservedStockById(itemId);
  const reservedStock = Number.parseInt(result || 0)
  productItem.currentQuantity = productItem.initialAvailableQuantity - reservedStock;
  if (productItem.currentQuantity < 1) {
    res.json({status: "Not enough stock available", itemId: 1});
    retuen;
  }
  reserveStockById(productItem.itemId, reservedStock + 1);
  res.json({status: "Reservation confirmed", itemId: productItem.itemId});
});

app.listen(1245, () => {
  console.log('Server running on localhost:1245');
});

export default app;
