const kue = require('kue');

const queue = kue.createQueue();

const job = queue.create('push_notification_code', {
  phoneNumber: '770727868',
  message: 'Hello Holberton',
})


job.on('complete', () => {
  console.log('Notification job completed');
})
.on('enqueue', () => {
  console.log('Notification job created:', job.id);
})
.on('failed', () => {
  console.log('Notification job failed');
});
  
job.save();
  
