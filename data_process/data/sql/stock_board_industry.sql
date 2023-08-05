create table `stock_board_industry`(
    `rank` int not null comment '排名',
    `board_name` varchar(64) not null comment '板块名称',
    `board_code` varchar(16) not null comment '板块代码',
    `newest_price` decimal(30, 10) not null comment '最新价',
    'tmp' varchar(8) not null comment '涨跌额',
    'tmp' varchar(8) not null comment '涨跌幅',
    'tmp' varchar(8) not null comment '总市值',
    'tmp' varchar(8) not null comment '换手率',
    'tmp' varchar(8) not null comment '上涨家数',
    'tmp' varchar(8) not null comment '下跌家数',
    'tmp' varchar(8) not null comment '领涨股票',
    'tmp' varchar(8) not null comment '领涨股票-涨跌幅',
) comment '行业板块';