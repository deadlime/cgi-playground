FROM httpd:2.4-alpine

RUN apk add --no-cache libc6-compat nodejs perl php82 python3 ruby

RUN sed -i 's/#LoadModule cgid_module /LoadModule cgid_module /g' /usr/local/apache2/conf/httpd.conf && \
    sed -i 's/#LoadModule cgi_module /LoadModule cgi_module /g' /usr/local/apache2/conf/httpd.conf && \
    sed -i 's/#LoadModule proxy_module /LoadModule proxy_module /g' /usr/local/apache2/conf/httpd.conf && \
    sed -i 's/#LoadModule proxy_scgi_module /LoadModule proxy_scgi_module /g' /usr/local/apache2/conf/httpd.conf && \
    sed -i 's/#LoadModule proxy_fcgi_module /LoadModule proxy_fcgi_module /g' /usr/local/apache2/conf/httpd.conf && \
    echo 'ProxyPass "/scgi-bin/" "scgi://scgi:9999/'>>/usr/local/apache2/conf/httpd.conf && \
    echo 'ProxyPass "/fcgi-bin/" "fcgi://fcgi:9999/'>>/usr/local/apache2/conf/httpd.conf
