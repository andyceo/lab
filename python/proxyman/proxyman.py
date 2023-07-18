#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Proxy Manager: the beginning. @see https://github.com/bergarces/ProxyManager"""
import csv
import os
from pathlib import Path
from sqlalchemy import Column, create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.types import Integer, String
from sqlalchemy.dialects.mysql import INTEGER
Base = declarative_base()
UnsignedInt = Integer()
UnsignedInt = UnsignedInt.with_variant(INTEGER(unsigned=True), 'mysql')


class Proxy(Base):
    """Proxy"""
    __tablename__ = 'proxy'
    id = Column(UnsignedInt, primary_key=True, autoincrement='auto')
    proxy = Column(String(32), unique=True, nullable=False)
    country = Column(String(2), unique=False, nullable=False)
    # @todo: port and IP denormalization
    # @see https://stackoverflow.com/questions/2542011/most-efficient-way-to-store-ip-address-in-mysql


if __name__ == '__main__':
    if 'PROXYMAN_PASSWORD' not in os.environ:
        raise Exception('Set PROXYMAN_PASSWORD environment variable containing MySQL password to continue...')

    # Prepare database connection and schema
    pswd = os.environ.get('PROXYMAN_PASSWORD')
    engine = create_engine(f"mysql+pymysql://proxyman:{pswd}@127.0.0.1:3306/proxyman", echo=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Parse csv file with proxies and delete it after
    path = Path(__file__).parent.resolve() / '../../../../Загрузки'
    file_path = path.resolve() / 'socks5.csv'  # download from https://hideip.me/ru/proxy/socks5list
    with open(file_path, "r", encoding='utf-8-sig', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in reader:
            row = [_.strip('').strip(' ."') for _ in row]
            proxy = Proxy(proxy=row[0], country=row[1])
            try:
                session.add(proxy)
                session.commit()
            except SQLAlchemyError as e:
                session.rollback()
    os.remove(file_path)
