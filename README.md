# 演示地址
- http://47.52.156.68:8080
（服务器位于香港，可能会有点慢）

# 功能说明
- 手写数字识别（鼠标在左侧方框写入数字，点击识别即可）

# 运行环境
- node8
- python3

确保全局安装 `parcel-bundler`，如果没安装请运行 `npm install -g parcel-bundler`；确保安装 python3 以及 tensorflow、flask、flask_cors、numpy 模块，python 模块可以通过 pip install 安装。windows 安装python 推荐安装 Anaconda。

# 本地配置
- npm install
- parcel index.html
- python api.py

# 线上配置
## 运行
- npm install
- parcel build index.html

## nginx 配置
```
server {
        listen 8080;

        server_name _;

        root /var/www/html/numerical-recognition/dist/; // 项目入口地址

        index index.html index.htm index.php index.nginx-debian.html;

        location / {
                # First attempt to serve request as file, then
                # as directory, then fall back to displaying a 404.
                # try_files $uri $uri/ =404;
                try_files $uri $uri/ /index.html;
        }
}
```
## supervisor 进程守护
python 服务由 Supervisor 启动并维护，设置参数如下：

```
[program:numerical-recognition]
process_name=%(program_name)s
command=python3 /var/www/html/numerical-recognition/api.py
autostart=true
autorestart=true
user=root
numprocs=1
redirect_stderr=false
stdout_logfile=/var/log/supervisor/numerical-recognition.log
```
如果启动失败，可能需要执行：`unlink /run/supervisor.sock`
- supervisord -c /etc/supervisor/supervisord.conf //起服务，注意 supervisor 配置文件所在目录
- supervisord shutdown //关闭服务
- supervisord reload //重启服务

# 项目布局

```
.
├── dist                                        // 项目打包路径
├── mnist                                       // 训练模型
│   ├── data                                    // 权重和偏置变量的存储路径
│   ├── convolutional.js                        // 卷积神经网络训练模型
│   ├── model.py                                // 变量和模型的创建
│   └── regression.py                           // 前馈神经网络训练模型
├── src                                         // 前端目录
│   ├── router
│   │   └── index.js                            // 路由配置
│   ├── App.vue                                 // 页面入口文件
│   ├── main.js                                 // 程序入口文件，加载各种公共组件
│   ├── canvas.js                               // 手写数字生成
│   └── MainPage.vue                            // 首页
├── index.html                                  // 入口 html 文件
├── api.py                                      // api 配置文件
├── .babelrc                                    // 设置转码的规则
└── postcss.config.js                           // 转换 CSS 
.

```

# 参考
- [https://github.com/sugyan/tensorflow-mnist](https://github.com/sugyan/tensorflow-mnist)
- [https://segmentfault.com/a/1190000012427886](https://segmentfault.com/a/1190000012427886)
- [https://laravue.org/#/articles/21](https://laravue.org/#/articles/21)
