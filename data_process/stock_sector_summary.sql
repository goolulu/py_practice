create table `stock_sector_summary`(
    `name` varchar(32) not null comment '项目名称',
    `en_name` varchar(32) not null comment '项目名称-英文',
    `trade_days` int not null comment '交易天数',
    `trade_amount` decimal(30) not null comment '成交金额-人民币元',
    `total_amount_ratio` decimal(10, 8) not null comment '成交金额-占总计',
    `trade_quantity` decimal(30) not null comment '成交股数-股数',
    `total_quantity_ratio` decimal(10, 8) not null comment '成交股数-占总计',
    `trade_valume` decimal(30) not null comment '成交笔数-笔',
    `total_valume_ratio` decimal(10, 8) not null comment '成交笔数-占总计',
    primary key pk_name(name)
);