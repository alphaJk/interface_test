from peewee import *


# 连接数据库
db = MySQLDatabase("wallet_dev", host="192.168.1.50", port=3306, user="wallet", passwd="wallet123")
db.connect()


class Transaction(Model):
    transaction_id = CharField(primary_key=True)
    from_id = CharField()
    transaction_type = IntegerField()
    to_id = CharField()
    coin_type = CharField()
    occur_amount = DecimalField()
    transfer_type = IntegerField()
    create_time  = DateTimeField()
    flow_no = CharField()
    merchant_id = BigIntegerField()
    operator_id = BigIntegerField()
    business_type = IntegerField()
    trans_status = IntegerField()
    remark = CharField()

    class Meta:
        database = db
        table_name = 'account_transaction'


if __name__ == '__main__':
    obj_db = Transaction.get(transaction_id='JY19522924946664')
    print(obj_db.create_time)
    print(obj_db.flow_no)