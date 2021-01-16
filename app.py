import threading
from common.init_config import application, config
from services.common.s_com import module_common,module_common_prefix
from services.files.s_file import module_file,module_file_prefix
import datetime

from util.IpUtil import printIpInfo


def install_config():
    """
    加载config文件
     schedule.add_job(func=sync_ev_health, trigger='cron', month='*', day='*', hour='1', id='job5')
    schedule.add_job(func=sync_maintain_date, trigger='interval', seconds=3600, id='job6')
    :return:
    """
    pass

def install_socket():
    """
    加载config文件
    启动socket
    :return:
    """
    pass


def printHello():
    print("------" + str(datetime.datetime.now()) + "------")
    timer = threading.Timer(5, printHello)
    timer.start()

if __name__ == "__main__":
    printIpInfo()
    # mq_thr = threading.Thread(target=install_config, name='MQThread')
    # mq_thr.daemon = True
    # mq_thr.start()

    # sq_thr = threading.Thread(target=install_socket, name='SOCKETThread')
    # sq_thr.daemon = True
    # sq_thr.start()

    application.register_blueprint(module_common, url_prefix=module_common_prefix)
    application.register_blueprint(module_file, url_prefix=module_file_prefix)

    application.run(
        host=config.listen,
        port=config.port,
        debug=config.debug,
        threaded=True
    )

    # socketio.run(application)
