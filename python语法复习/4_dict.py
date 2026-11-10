contact={('张三', 23): "123456789", ('张三', 24): "987654321"}

print(contact)
print(contact[('张三', 23)])
contact[('张三', 23)] = "111111111"
print(contact[('张三', 23)])
contact[('李四', 25)] = "222222222"
print(contact)
contact.update({('王五', 26): "333333333"})
for key, value in contact.items():
    print(key, value)