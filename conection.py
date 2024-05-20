

nuevo_usuario = (4265982, 'David', 'Chavarria Mazo', 31043713,'davicha95@gmail.com','cr 129 67-260','Pedregal','Medellin','Colombia')

# consulta = 'INSERT INTO appointment.date_pct (identification_pct, name_pct, lastname_pct, phone, email, address, barrium, city, country) VALUES (%s, %s)'
consulta = ('INSERT INTO appointment.date_pct '
            '(identification_pct, name_pct, lastname_pct, phone, email, address, barrium, city, country) '
            'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)')

