from apscheduler.schedulers.background import BackgroundScheduler
#from .tasks import send_mails

appointment_scheduler = BackgroundScheduler()
appointment_scheduler.add_job(
    id='send_mails',
    func=lambda: print('123'),
    trigger='interval',
)