FROM tiangolo/uwsgi-nginx-flask:python3.6

# Install sdcv dictionary
RUN apt update
RUN apt install sdcv
RUN wget -nv http://download.huzheng.org/dict.org/stardict-dictd_www.dict.org_gcide-2.4.2.tar.bz2
RUN mkdir -p /root/.stardict/dic
RUN tar -C /root/.stardict/dic -xf stardict-dictd_www.dict.org_gcide-2.4.2.tar.bz2

