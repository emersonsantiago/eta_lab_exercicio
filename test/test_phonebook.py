from src.phonebook import Phonebook


class TestPhonebook:


    def test_add_phone(self):
        #Setup
        phonebook = Phonebook()
        expected_result = "Número adicionado"

        #Chamada
        result = phonebook.add("Emerson", "81998743079")

        #Validação
        assert result == expected_result


    def test_add_phone_invalid_name_hashtag(self):
        # Setup
        phonebook = Phonebook()
        expected_result = "Nome inválido"

        # Chamada
        result = phonebook.add("Joao #", "81998743079")

        # Validação
        assert result == expected_result


    def test_add_phone_invalid_name_at(self):
        # Setup
        phonebook = Phonebook()
        expected_result = "Nome inválido"

        # Chamada
        result = phonebook.add("Joao @", "81998743079")

        # Validação
        assert result == expected_result


    def test_add_phone_invalid_name_exclamation(self):
        # Setup
        phonebook = Phonebook()
        expected_result = "Nome inválido"

        # Chamada
        result = phonebook.add("Joao !", "81998743079")

        # Validação
        assert result == expected_result


    def test_add_phone_invalid_name_cipher(self):
        # Setup
        phonebook = Phonebook()
        expected_result = "Nome inválido"

        # Chamada
        result = phonebook.add("Joao $", "81998743079")

        # Validação
        assert result == expected_result


    def test_add_phone_invalid_name_percent(self):
        # Setup
        phonebook = Phonebook()
        expected_result = "Nome inválido"

        # Chamada
        result = phonebook.add("Joao %", "81998743079")

        # Validação
        assert result == expected_result


    def test_add_phone_invalid_number(self):
        #Setup
        phonebook = Phonebook()
        expected_result = "Número inválido"

        #Chamada
        result = phonebook.add("Joao José", "")

        #Validação
        assert result == expected_result



    def test_lookup_phone_invalid_name_hashtag(self):
        # Setup
        phonebook = Phonebook()
        expected_result = "Nome inválido"

        # Chamada
        result = phonebook.lookup("Joao #")

        # Validação
        assert result == expected_result


    def test_lookup_phone_invalid_name_at(self):
        # Setup
        phonebook = Phonebook()
        expected_result = "Nome inválido"

        # Chamada
        result = phonebook.lookup("Joao @")

        # Validação
        assert result == expected_result


    def test_lookup_phone_invalid_name_exclamation(self):
        # Setup
        phonebook = Phonebook()
        expected_result = "Nome inválido"

        # Chamada
        result = phonebook.lookup("Joao !")

        # Validação
        assert result == expected_result


    def test_lookup_phone_invalid_name_cipher(self):
        # Setup
        phonebook = Phonebook()
        expected_result = "Nome inválido"

        # Chamada
        result = phonebook.lookup("Joao $")

        # Validação
        assert result == expected_result


    def test_lookup_phone_invalid_name_percent(self):
        # Setup
        phonebook = Phonebook()
        expected_result = "Nome inválido"

        # Chamada
        result = phonebook.lookup("Joao %")

        # Validação
        assert result == expected_result


    def test_lookup_phone_valid_name(self):
        # Setup
        phonebook = Phonebook()
        expected_result = "190"

        # Chamada
        result = phonebook.lookup("POLICIA")

        # Validação
        assert result == expected_result


    def test_get_names(self):
        # Setup
        phonebook = Phonebook()
        phonebook.add("Emerson", "81998743079")
        expected_result = ["Emerson", "POLICIA"]

        # Chamada
        result = phonebook.get_names()

        # Validação
        assert sorted(result) == sorted(expected_result)


    def test_get_name_by_number(self):
        # Setup
        phonebook = Phonebook()
        expected_result = "POLICIA"

        # Chamada
        result = phonebook.get_name_by_number("190")

        # Validação
        assert result == expected_result


    def test_get_name_by_number_doesnt_exist(self):
        # Setup
        phonebook = Phonebook()
        expected_result = "Número não encontrado"

        # Chamada
        result = phonebook.get_name_by_number("100")

        # Validação
        assert result == expected_result


    def test_change_number(self):
        # Setup
        phonebook = Phonebook()
        expected_result = "Número foi modificado"

        # Chamada
        result = phonebook.change_number("POLICIA", "180")

        # Validação
        assert result == expected_result


    def test_change_number_error(self):
        # Setup
        phonebook = Phonebook()
        expected_result = "Número não foi modificado"

        # Chamada
        result = phonebook.change_number("Emarson", "9090")

        # Validação
        assert result == expected_result


    def test_delete_number(self):
        # Setup
        phonebook = Phonebook()
        expected_result = "Número foi deletado"
        phonebook.add("Emerson", "1818")

        # Chamada
        result = phonebook.delete("Emerson")

        # Validação
        assert result == expected_result



    def test_clear(self):
        # Setup
        phonebook = Phonebook()
        expected_result = "phonebook limpado"

        # Chamada
        result = phonebook.clear()

        # Validação
        assert result == expected_result


    def test_add_phone_already_exists(self):
        #Setup
        phonebook = Phonebook()
        expected_result = "Número adicionado"

        #Chamada
        result = phonebook.add("POLICIA", "190")

        #Validação
        assert result == expected_result