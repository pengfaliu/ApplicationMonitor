# ApplicationMonitor
这个监控器是基于Python语言写的，只是一个第一个初级版本，主要用于从数据库获取相应数据，然后通过邮箱或短信的方式定时发送报告。如果大家好的想法可以提交上来，我们一起完成

#目录说明
#### Applications 

**该目录表示具体的应用脚本及功能，可以以目录区分监控不同的应用。** 

#### ConfigureFilePaser 

**该目录是整个Monitor的监控全局配置文件的解析库**

#### DataBaseOperator 

**这个目录是数据库操作器，自定的功能类。目前包含，oracle操作类，mysql操作类，后续可以补充其他数据的库的操作类**

#### ExcelGenerator

**这个目录是当应用监控的结果需要生成excel文件时，这里有你需要的模块** 	
#### HtmlGenerator	
**这个目录是当你想生成html代码时，这里有你需要的模块和模板**

#### SendMessage 
**这里是监控需要的结果发送器，有短信发送器，有邮件发送器**

#### ThirdPartyModule
**在这里是一些不常用的第三方模板的集合，需要的时候可以在这里找，也可以下载放在这里，以备不时之需。**
