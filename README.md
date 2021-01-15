# my_test

### 用途：
1.用于API自动化测试 <br>
2.用于服务端测试 <br>

### 使用说明
### 一、API自动化测试 
详见module中的api_test <br>

### 二、服务端测试 
配置服务端相关：<br>
1.[common.ini](https://github.com/yingtian648/my_test/blob/master/config/common.ini) 主要用于配置本地(局域网内)访问ip及端口，本地文件存储地址，日志级别 <br>
2.[app.py](https://github.com/yingtian648/my_test/blob/master/app.py) 是主启动python文件，用于启动整个服务端项目。（服务以蓝图的方式分模块注册） <br>
3.[services](https://github.com/yingtian648/my_test/tree/master/services) 目录用于放置服务层，dao层，control层代码(init.py中有简略说明) <br>
