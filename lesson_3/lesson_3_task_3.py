from address import Address
from mailing import Mailing

to_address = Address(123456, 'Moscow', 'Lenin', 1, 101)
from_address = Address(654321, 'Moscow', 'Petrov', 2, 202)
mail_ = Mailing(to_address, from_address, 101, 'yes')

print(f"Отправление <{mail_.track}> из <{mail_.from_address.index}>, <{mail_.from_address.city}>, <{mail_.from_address.street}>, <{mail_.from_address.house}> - <{mail_.from_address.flat}> в <{mail_.to_address.index}>, <{mail_.to_address.city}>, <{mail_.to_address.street}>, <{mail_.to_address.house}> -<{mail_.to_address.flat}>. Стоимость <{mail_.cost}> рублей.")