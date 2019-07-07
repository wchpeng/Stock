class BaseTemplate:
    pk = 10
    name = "san"

    class Meta:
        db_name = "base_template"


class NewCls:

    _instance = {}

    def __new__(cls, base_cls, tb_name):
        new_tb_name = "%s_To_%s" % (base_cls.__name__, tb_name)

        if new_tb_name not in cls._instance:
            new_tb_meta = base_cls.Meta
            new_tb_meta.db_name = tb_name
            new_tb = type(new_tb_name, (base_cls,), {"Meta": new_tb_meta, "__module__": cls.__module__, "__tablename__": tb_name})
            cls._instance[tb_name] = new_tb
        return cls._instance[tb_name]

a = NewCls(BaseTemplate, 'table001')
b = NewCls(BaseTemplate, 'table002')
c = NewCls(BaseTemplate, 'table003')
