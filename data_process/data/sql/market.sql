create table `market_stock_summary`(
    `assets_type` varchar(32) not null comment '证券类别',
    `quantity` decimal(20) null default 0.0 comment '数量',
    `balance` decimal(30) null default 0.0 comment '成交金额',
    `total_market_value` decimal(30) null default 0.0 comment '总市值',
    `liquid_market_value` decimal(30) null default 0.0 comment '流动市值',
    `trade_date` varchar(8) not null comment '交易日',
    primary key pk_market_stock_summary(assets_type, trade_date)
);