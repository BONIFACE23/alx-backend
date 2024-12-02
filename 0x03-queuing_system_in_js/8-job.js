const createPushNotificationsJobs = (jobs, queue) => {
  if (!(jobs instanceof Array)) {
    throw Error('Jobs is not an array');
  } else {
    jobs.forEach(job => {
      const que = queue.create('push_notification_code_3', job);
      que.on('complete', () => {
          console.log(`Notification job ${que.id} completed`);
        })
        .on('enqueue', () => {
          console.log('Notification job created:', que.id);
        })
        .on('failed', (err) => {
          console.log(`Notification job ${que.id} failed: ${err}`);
        }).on('progress', (progress) => {
          console.log(`Notification job ${que.id} ${progress}% complete`);
        });
          
      que.save();
    })
  }
}

export default createPushNotificationsJobs;
