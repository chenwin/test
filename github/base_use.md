####提交时转换为LF，检出时转换为CRLF
git config --global core.autocrlf true   

####提交时转换为LF，检出时不转换
git config --global core.autocrlf input   

####提交检出均不转换
git config --global core.autocrlf false

####配置用户
git config --global user.name "XXX"

git config --global user.email "XXX@XXXXXX.com"

