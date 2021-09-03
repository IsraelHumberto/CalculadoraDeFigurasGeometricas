def titulo_area(titulo):
    print('--' * 30)
    print(titulo.upper())
    print('--' * 30)


titulo_area('calculadora geométrica')


def opcao():
    opcao_area = int(input('Escolha uma forma geométrica:\n'
                           '1 - Quadrado\n'
                           '2 - Círculo\n'
                           '3 - Retângulo\n'
                           '4 - Triângulo\n'))

    if opcao_area == 1:
        calcularAreaQuadrado()
    elif opcao_area == 2:
        calcularAreaCirculo()
    elif opcao_area == 3:
        calcularAreaRetangulo()
    elif opcao_area == 4:
        calcularAreaTriangulo()
    else:
        opcao()


def calcularAreaQuadrado():
    """Função para calcular área do quadrado"""
    titulo_area('area do quadrado')

    lado_quad = float(input('Informe o tamanho do lado: '))
    area_quad = lado_quad ** 2

    print(f'A área do quadrado é: {area_quad}m²\n')


def calcularAreaCirculo():
    """Função para calcular área do circulo"""
    titulo_area('area do circulo')

    pi = 3.1415
    raio_circ = float(input('Informe o raio do círculo: '))
    area_circ = pi * raio_circ ** 2

    print(f'A área do círculo é: {area_circ}m²\n')


def calcularAreaRetangulo():
    """Função para calcular área do retângulo"""
    titulo_area('area do retângulo')

    alt_ret = float(input('Informe a altura: '))
    larg_ret = float(input('Informe a largura: '))
    area_retangulo = alt_ret * larg_ret

    print(f'A área do retângulo é: {area_retangulo}m²\n')


def calcularAreaTriangulo():
    """Função para calcular área do triângulo"""
    titulo_area('area do triângulo')

    alt_triangulo = float(input('Informe a altura: '))
    base_triangulo = float(input('Informe a base: '))
    area_triangulo = alt_triangulo * base_triangulo / 2

    print(f'A área do triângulo é: {area_triangulo}m²\n')


while True:
    opcao()
