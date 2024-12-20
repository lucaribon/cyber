FROM php:apache

MAINTAINER Zane Durkin <zane@neverlanctf.com>

RUN apt-get update --fix-missing
RUN a2enmod rewrite

COPY web/ /var/www/html
