import { expect } from 'chai';
import { createQueue } from 'kue';
import createPushNotificationsJobs from './8-job.js';


describe('createPushNotificationsJobs', async () => {
  const queue = createQueue({ name: 'push_notification_code_test' });

  beforeEach(() => {
    queue.testMode.enter(true);
  });

  after(() =>  {
    queue.testMode.clear();
    queue.testMode.exit()
  });

  it('displays an error message if jobs is not an array', () => {
    expect(
      createPushNotificationsJobs.bind(createPushNotificationsJobs, {}, queue)
    ).to.throw('Jobs is not an array');
  });

  it('should create jobs in the queue', () => {
    createPushNotificationsJobs([{ phoneNumber: '+1234567890', message: 'Test message 1' }], queue);

    expect(queue.testMode.jobs.length).to.equal(1);
    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');

    const jobData = queue.testMode.jobs[0].data;
    expect(jobData.phoneNumber).to.equal('+1234567890');
    expect(jobData.message).to.equal('Test message 1');
  });
})
