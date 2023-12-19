def cria_posicao(x, y):
    """cria_posicao: int × int → posicao

    Esta função recebe os valores correspondentes às coordenadas de uma posição e devolve a posição correspondente. Ela
    também verifica a validade dos argumentos."""
    if type(x) != int or type(y) != int or x < 0 or y < 0:
        raise ValueError("cria_posicao: argumentos invalidos")
    return x, y


def cria_copia_posicao(p):
    """cria_copia_posicao: posicao → posicao

    Esta função recebe uma posição e devolve uma cópia nova da posição."""
    new_p = ()
    for e in p:
        new_p += (e,)
    return new_p


def obter_pos_x(p):
    """obter_pos_x: posicao → int

    Esta função recebe uma posição e devolve a componente x dela."""
    return p[0]


def obter_pos_y(p):
    """obter_pos_y: posicao → int

        Esta função recebe uma posição e devolve a componente y dela."""
    return p[1]


def eh_posicao(arg):
    """eh_posicao: universal → booleano

    Esta função devolve True caso o seu argumento seja um TAD posição e False caso contrário."""
    if type(arg) != tuple or len(arg) != 2 or type(arg[0]) != int or type(arg[1]) != int or arg[0] < 0 or arg[1] < 0:
        return False
    return True


def posicoes_iguais(p1, p2):
    """posicoes_iguais: posicao × posicao → booleano

    Esta função devolve True apenas se p1 e p2 são posições e são iguais."""
    if eh_posicao(p1) and eh_posicao(p2) and obter_pos_x(p1) == obter_pos_x(p2) and obter_pos_y(p1) == obter_pos_y(p2):
        return True
    return False


def posicao_para_str(p):
    """posicao_para_str: posicao → str

    Esta função devolve a cadeia de caracteres ‘(x, y)’ que representa o seu argumento, sendo os valores x e y as
    coordenadas de p."""
    return "(" + str(obter_pos_x(p)) + ", " + str(obter_pos_y(p)) + ")"


def obter_posicoes_adjacentes(p):
    """obter_posicoes_adjacentes: posicao → tuplo

    Esta função devolve um tuplo com as posições adjacentes à posição p, começando pela posição acima de p e seguindo no
    sentido horário."""
    if obter_pos_y(p)-1 <= 0 and obter_pos_x(p)-1 <= 0:
        return (obter_pos_x(p) + 1, obter_pos_y(p)), (obter_pos_x(p), obter_pos_y(p) + 1)
    elif obter_pos_y(p)-1 <= 0 and obter_pos_x(p)-1 >= 0:
        return (obter_pos_x(p) + 1, obter_pos_y(p)), (obter_pos_x(p), obter_pos_y(p) + 1), (obter_pos_x(p) - 1,
                                                                                            obter_pos_y(p))
    elif obter_pos_x(p)-1 <= 0 and obter_pos_y(p)-1 >= 0:
        return (obter_pos_x(p), obter_pos_y(p) - 1), (obter_pos_x(p) + 1, obter_pos_y(p)), (obter_pos_x(p),
                                                                                            obter_pos_y(p) + 1)
    elif obter_pos_x(p)-1 >= 0 and obter_pos_y(p)-1 >= 0:
        return (obter_pos_x(p), obter_pos_y(p)-1), (obter_pos_x(p)+1, obter_pos_y(p)), \
               (obter_pos_x(p), obter_pos_y(p)+1), (obter_pos_x(p)-1, obter_pos_y(p))


def ordenar_posicoes(t):
    """ordenar_posicoes: tuplo → tuplo

    Esta função devolve um tuplo contendo as mesmas posições do tuplo fornecido como argumento, ordenadas de acordo com
    a ordem de leitura do prado."""
    return tuple(sorted(sorted(t), key=lambda x: x[1]))


def cria_animal(s, r, a):
    """cria_animal: str × int × int → animal

    Esta função recebe uma cadeia de caracteres "s" não vazia correspondente à espécie do animal e dois valores inteiros
    correspondentes à frequência de reprodução "r" (maior do que 0) e à frequência de alimentação "a" (maior ou igual
    que 0); e devolve o animal."""
    if type(s) != str or s == "" or type(r) != int or r <= 0 or type(a) != int or a < 0:
        raise ValueError("cria_animal: argumentos invalidos")
    return {"especie": s, "reprod": r, "alimen": a, "idade": 0, "fome": 0}


def cria_copia_animal(a):
    """cria_copia_animal: animal → animal

    Esta função recebe um animal "a" (predador ou presa) e devolve uma nova cópia do animal."""
    new_a = a.copy()
    return new_a


def obter_especie(a):
    """obter_especie: animal → str

    Esta função devolve a cadeia de caracteres correspondente à espécie do animal."""
    return a["especie"]


def obter_freq_reproducao(a):
    """obter_freq_reproducao: animal → int

    Esta função devolve a frequência de reproduçãao do animal "a"."""
    return a["reprod"]


def obter_freq_alimentacao(a):
    """obter_freq_alimentacao: animal → int

    Esta função devolve a frequência de alimentação do animal "a" (as presas devolvem sempre 0)."""
    return a["alimen"]


def obter_idade(a):
    """obter_idade: animal → int

    Esta função devolve a idade do animal "a"."""
    return a["idade"]


def obter_fome(a):
    """obter_fome: animal → int

    Esta função devolve a fome do animal "a" (as presas devolvem sempre 0)."""
    return a["fome"]


def aumenta_idade(a):
    """aumenta_idade: animal → animal

    Esta função modifica destrutivamente o animal "a" incrementando o valor da sua idade em uma unidade, e devolve o
    próprio animal."""
    a["idade"] += 1
    return a


def reset_idade(a):
    """reset_idade: animal → animal

    Esta função modifica destrutivamente o animal "a" definindo o valor da sua idade como 0, e devolve o próprio animal.
    """
    a["idade"] = 0
    return a


def aumenta_fome(a):
    """aumenta_fome: animal → animal

    Esta função modifica destrutivamente o animal predador "a" incrementando o valor da sua fome em uma unidade, e
    devolve o próprio animal. Esta operação não modifica os animais presa."""
    a["fome"] += 1
    return a


def reset_fome(a):
    """reset_fome: animal → animal

    Esta função modifica destrutivamente o animal predador "a" definindo o valor da sua fome como 0, e devolve o próprio
    animal. Esta operação não modifica os animais presa."""
    a["fome"] = 0
    return a


def eh_animal(arg):
    """eh_animal: universal → booleano

    Esta função devolve True caso o seu argumento seja um TAD animal e False caso contrário."""
    if type(arg) != dict or len(arg) != 5 or "especie" not in arg or type(arg["especie"]) != str or arg["especie"] \
            == "" or "reprod" not in arg or type(arg["reprod"]) != int or arg["reprod"] <= 0 or "alimen" not in arg or \
            type(arg["alimen"]) != int or arg["alimen"] < 0 or "idade" not in arg or type(arg["idade"]) != int or \
            arg["idade"] < 0 or "fome" not in arg or type(arg["fome"]) != int or arg["fome"] < 0:
        return False
    return True


def eh_predador(arg):
    """eh_predador: universal → booleano

    Esta função devolve True caso o seu argumento seja um TAD animal do tipo predador e False caso contrário."""
    return eh_animal(arg) and obter_freq_alimentacao(arg) != 0


def eh_presa(arg):
    """eh_presa: universal → booleano

    Esta função devolve True caso o seu argumento seja um TAD animal do tipo presa e False caso contrário."""
    return eh_animal(arg) and obter_freq_alimentacao(arg) == 0 and obter_fome(arg) == 0


def animais_iguais(a1, a2):
    """animais_iguais: animal × animal → booleano

    Esta função devolve True apenas se a1 e a2 são animais e são iguais."""
    if not eh_animal(a1) or not eh_animal(a2) or obter_especie(a1) != obter_especie(a2) or obter_freq_reproducao(a1) \
            != obter_freq_reproducao(a2) or obter_freq_alimentacao(a1) != obter_freq_alimentacao(a2) or obter_idade(a1)\
            != obter_idade(a2) or obter_fome(a1) != obter_fome(a2):
        return False
    return True


def animal_para_char(a):
    """animal_para_char: animal → str

    Esta função devolve a cadeia de caracteres dum único elemento correspondente ao primeiro carácter da espécie do
    animal passada por argumento, em maiúscula para animais predadores e em min ́uscula para animais presa."""
    if eh_predador(a):
        return obter_especie(a)[0].upper()
    else:
        return obter_especie(a)[0].lower()


def animal_para_str(a):
    """animal_para_str: animal → str

    Esta função devolve a cadeia de caracteres que representa o animal, sendo esta a sua espécie, seguido da sua idade e
    com qual idade irá reproduzir e da sua fome e frequência de alimentação, entre parênteses retos."""
    if eh_presa(a):
        return obter_especie(a) + " [" + str(obter_idade(a)) + "/" + str(obter_freq_reproducao(a)) + "]"
    else:
        return obter_especie(a) + " [" + str(obter_idade(a)) + "/" + str(obter_freq_reproducao(a)) + ";" + \
               str(obter_fome(a)) + "/" + str(obter_freq_alimentacao(a)) + "]"


def eh_animal_fertil(a):
    """eh_animal_fertil: animal → booleano

    Esta função devolve True caso o animal a tenha atingido a idade de reprodução e False caso contrário."""
    return obter_idade(a) == obter_freq_reproducao(a)


def eh_animal_faminto(a):
    """eh_animal_faminto: animal → booleano

    Esta função devolve True caso o animal a tenha atingindo um valor de fome igual ou superior à sua frequência de
    alimentação e False caso contrário. As presas devolvem sempre False."""
    if eh_presa(a):
        return False
    else:
        return obter_fome(a) >= obter_freq_alimentacao(a)


def reproduz_animal(a):
    """reproduz_animal: animal → animal

    Esta função recebe um animal "a", devolvendo um novo animal da mesma espécie com idade e fome igual a 0, e
    modificando destrutivamente o animal passado como argumento "a", alterando a sua idade para 0."""
    reset_idade(a)
    return reset_fome(cria_copia_animal(a))


def cria_prado(d, r, a, p):
    """cria_prado: posicao × tuplo × tuplo × tuplo → prado

    Esta função recebe uma posição "d" correspondente à posição que ocupa a montanha do canto inferior direito do prado,
    um tuplo "r" de 0 ou mais posições correspondentes aos rochedos que não são as montanhas dos limites exteriores do
    prado, um tuplo a de 1 ou mais animais, e um tuplo "p" da mesma dimensão do tuplo a com as posições correspondentes
    ocupadas pelos animais; e devolve o prado que representa internamente o mapa e os animais presentes."""
    if not eh_posicao(d) or type(r) != tuple:
        raise ValueError("cria_prado: argumentos invalidos")
    for pos in r:
        if not eh_posicao(pos) or obter_pos_x(pos) == 0 or obter_pos_x(pos) >= d[0] or obter_pos_y(pos) == 0 or \
                obter_pos_y(pos) >= d[1]:
            raise ValueError("cria_prado: argumentos invalidos")
    if type(a) != tuple or len(a) == 0 or type(p) != tuple or len(p) != len(a):
        raise ValueError("cria_prado: argumentos invalidos")
    for animal in a:
        if not eh_animal(animal):
            raise ValueError("cria_prado: argumentos invalidos")
    for pos in p:
        if not eh_posicao(pos) or pos in r or obter_pos_x(pos) == 0 or obter_pos_x(pos) == d[0] or obter_pos_y(pos) \
                == 0 or obter_pos_y(pos) == d[1]:
            raise ValueError("cria_prado: argumentos invalidos")
    return {"dimensao": d, "rochedos": r, "animais": a, "posicoes_a": p}


def cria_copia_prado(m):
    """cria_copia_prado: prado → prado

    Esta função recebe um prado e devolve uma nova cópia do prado."""
    new_m = m.copy()
    return new_m


def obter_tamanho_x(m):
    """obter_tamanho_x: prado → int

    Esta função devolve o valor inteiro que corresponde à dimensão Nx do prado."""
    return obter_pos_x(m["dimensao"]) + 1


def obter_tamanho_y(m):
    """obter_tamanho_y: prado → int

    Esta função devolve o valor inteiro que corresponde à dimensão Ny do prado."""
    return obter_pos_y(m["dimensao"]) + 1


def obter_numero_predadores(m):
    """obter_numero_predadores: prado → int

    Esta função devolve o número de animais predadores no prado."""
    count = 0
    for animal in m["animais"]:
        if eh_predador(animal):
            count += 1
    return count


def obter_numero_presas(m):
    """obter_numero_presas: prado → int

    Esta função devolve o número de animais presa no prado."""
    count = 0
    for animal in m["animais"]:
        if eh_presa(animal):
            count += 1
    return count


def obter_posicao_animais(m):
    """obter_posicao_animais: prado → tuplo posicoes

    Esta função devolve um tuplo contendo as posições do prado ocupadas por animais, ordenadas em ordem de leitura do
    prado."""
    t = m["posicoes_a"]
    return tuple(sorted(sorted(t), key=lambda x: x[1]))


def obter_animal(m, p):
    """obter_animal: prado × posicao → animal

    Esta função devolve o animal do prado que se encontra na posição p."""
    for pos in m["posicoes_a"]:
        if pos == p:
            indice = m["posicoes_a"].index(pos)
            return m["animais"][indice]


def eliminar_animal(m, p):
    """eliminar_animal: prado × posicao → prado

    Esta função modifica destrutivamente o prado "m" eliminando o animal da posição "p" deixando-o livre. Devolve o
    próprio prado."""
    new_p = ()
    indice = -1
    for pos in m["posicoes_a"]:
        if pos != p:
            new_p += (pos,)
        else:
            indice = m["posicoes_a"].index(pos)
    m["posicoes_a"] = new_p
    m["animais"] = m["animais"][:indice] + m["animais"][indice + 1:]
    return m


def mover_animal(m, p1, p2):
    """mover_animal: prado × posicao × posicao → prado

    Esta função modifica destrutivamente o prado "m" movimentando o animal da posição "p1" para a nova posição "p2",
    deixando livre a posição onde se encontrava. Devolve o próprio prado."""
    m["animais"] += (obter_animal(m, p1),)
    m["posicoes_a"] += (p2,)
    eliminar_animal(m, p1)
    return m


def inserir_animal(m, a, p):
    """inserir_animal: prado × animal × posicao → prado

    Esta função modifica destrutivamente o prado "m", acrescentando na posição "p" do prado o animal a passado como
    argumento. Devolve o próprio prado."""
    m["animais"] += (a,)
    m["posicoes_a"] += (p,)
    return m


def eh_prado(arg):
    """eh_prado: universal → booleano

    Esta função devolve True caso o seu argumento seja um TAD prado e False caso contrário."""
    return type(arg) == dict and len(arg) == 4 and "dimensao" in arg and eh_posicao(arg["dimensao"]) and "rochedos" in \
        arg and type(arg["rochedos"]) == tuple and (eh_posicao(pos) and pos[0] != 0 and pos[0] != arg["dimensao"][0]
                                                    and pos[1] != 0 and pos[1] != arg["dimensao"][1] for pos in
                                                    arg["rochedos"]) and "animais" in arg and type(arg["animais"]) \
        == tuple and len(arg["animais"]) > 0 and (eh_animal(a) for a in arg["animais"]) and "posicoes_a" in arg and \
        type(arg["posicoes_a"]) == tuple and len(arg["posicoes_a"]) == len(arg["animais"]) and (eh_posicao(pos) and
                                                                                                pos not in
                                                                                                arg["rochedos"] and
                                                                                                pos[0] != 0 and
                                                                                                pos[0] !=
                                                                                                arg["dimensao"][0]
                                                                                                and pos[1] != 0 and
                                                                                                pos[1] !=
                                                                                                arg["dimensao"][1]
                                                                                                for pos in
                                                                                                arg["posicoes_a"])


def eh_posicao_animal(m, p):
    """eh_posicao_animal: prado × posicao → booleano

    Esta função devolve True apenas no caso da posição "p" do prado estar ocupada por um animal."""
    return p in m["posicoes_a"]


def eh_posicao_obstaculo(m, p):
    """eh_posicao_obstaculo: prado × posicao → booleano

    Esta função devolve True apenas no caso da posição "p" do prado corresponder a uma montanha ou rochedo."""
    return p in m["rochedos"] or obter_pos_x(p) == 0 or obter_pos_y(p) == 0 or obter_pos_x(p) ==\
        obter_pos_x(m["dimensao"]) or obter_pos_y(p) == obter_pos_y(m["dimensao"])


def eh_posicao_livre(m, p):
    """eh_posicao_livre: prado × posicao → booleano

    Esta função devolve True apenas no caso da posição "p" do prado corresponder a um espaço livre (sem animais nem
    obstáculos)."""
    return not eh_posicao_obstaculo(m, p) and not eh_posicao_animal(m, p)


def prados_iguais(m1, m2):
    """prados_iguais: prado × prado → booleano

    Esta função devolve True apenas se m1 e m2 forem prados e forem iguais."""
    return eh_prado(m1) and eh_prado(m2) and m1["dimensao"] == m2["dimensao"] and m1["rochedos"] == m2["rochedos"] and \
        m1["animais"] == m2["animais"] and m1["posicoes_a"] == m2["posicoes_a"]


def prado_para_str(m):
    """prado_para_str: prado → str

    Esta função devolve uma cadeia de caracteres que representa o prado como mostrado nos exemplos."""
    prado = ""
    for linha in range(obter_tamanho_y(m)):
        if linha == 0:
            prado += "+" + "-" * (m["dimensao"][0] - 1) + "+" + "\n"
        elif linha == m["dimensao"][1]:
            prado += "+" + "-" * (m["dimensao"][0] - 1) + "+"
        else:
            new_line = ""
            for coluna in range(1, m["dimensao"][0]):
                if eh_posicao_livre(m, cria_posicao(coluna, linha)):
                    new_line += "."
                elif eh_posicao_obstaculo(m, cria_posicao(coluna, linha)):
                    new_line += "@"
                else:
                    new_line += animal_para_char(obter_animal(m, cria_posicao(coluna, linha)))
            prado += "|" + new_line + "|" + "\n"
    return prado


def obter_valor_numerico(m, p):
    """obter_valor_numerico: prado × posicao → int

    Esta função devolve o valor numérico da posição "p" correspondente à ordem de leitura no prado "m"."""
    return obter_pos_y(p) * obter_tamanho_x(m) + obter_pos_x(p)


def obter_movimento(m, p):
    """obter_movimento: prado × posicao → posicao

    Esta função devolve a posição seguinte do animal na posição "p" dentro do prado "m" de acordo com as regras de
    movimento dos animais no prado."""
    adjacentes = obter_posicoes_adjacentes(p)
    possibilidades = len(adjacentes)
    p_com_presas = 0  # Possibilidades com presas
    adj_com_presas = ()
    i = 0
    while i < possibilidades:
        if eh_posicao_obstaculo(m, adjacentes[i]) or (eh_posicao_animal(m, adjacentes[i]) and
                                                      eh_predador(obter_animal(m, adjacentes[i]))):
            possibilidades -= 1
            adjacentes = adjacentes[:i] + adjacentes[i + 1:]
            i = -1
        i += 1
    if eh_predador(obter_animal(m, p)):
        i = 0
        while i < possibilidades:
            if eh_posicao_animal(m, adjacentes[i]) and eh_presa(obter_animal(m, adjacentes[i])):
                p_com_presas += 1
                adj_com_presas += (adjacentes[i],)
            i += 1
        if p_com_presas != 0:
            return adj_com_presas[obter_valor_numerico(m, p) % p_com_presas]
        else:
            if possibilidades == 0:
                return p
            else:
                return adjacentes[obter_valor_numerico(m, p) % possibilidades]
    if eh_presa(obter_animal(m, p)):
        i = 0
        while i < possibilidades:
            if eh_posicao_animal(m, adjacentes[i]) and eh_presa(obter_animal(m, adjacentes[i])):
                possibilidades -= 1
                adjacentes = adjacentes[:i] + adjacentes[i + 1:]
                i = -1
            i += 1
        if possibilidades == 0:
            return p
        else:
            return adjacentes[obter_valor_numerico(m, p) % possibilidades]


def geracao(m):
    """geracao: prado → prado

    Esta função modifica o prado "m" fornecido como argumento de acordo com a evolução correspondente a uma geração
    completa, e devolve o próprio prado. Isto é, seguindo a ordem de leitura do prado, cada animal (vivo) realiza o seu
    turno de ação de acordo com as regras descritas."""
    for linha in range(1, m["dimensao"][1]):
        for coluna in range(1, m["dimensao"][0]):
            pos_anterior = cria_posicao(coluna, linha)
            if eh_posicao_animal(m, pos_anterior) and "check" not in obter_animal(m, pos_anterior):
                # "check" é uma forma de verificar se o animal já se movimentou nesta geração
                nova_pos = obter_movimento(m, pos_anterior)
                if pos_anterior != nova_pos:
                    if nova_pos in m["posicoes_a"]:
                        if eh_predador(obter_animal(m, pos_anterior)) and eh_presa(obter_animal(m, nova_pos)):
                            eliminar_animal(m, nova_pos)
                            mover_animal(m, pos_anterior, nova_pos)
                            reset_fome(obter_animal(m, nova_pos))
                            aumenta_idade(obter_animal(m, nova_pos))
                    else:
                        if eh_predador(obter_animal(m, pos_anterior)) and not eh_presa(obter_animal(m, nova_pos)):
                            mover_animal(m, pos_anterior, nova_pos)
                            aumenta_fome(obter_animal(m, nova_pos))
                            aumenta_idade(obter_animal(m, nova_pos))
                        elif eh_presa(obter_animal(m, pos_anterior)):
                            mover_animal(m, pos_anterior, nova_pos)
                            aumenta_idade(obter_animal(m, nova_pos))
                    obter_animal(m, nova_pos)["check"] = 1
                    if eh_animal_fertil(obter_animal(m, nova_pos)) and nova_pos != pos_anterior:
                        novo = reproduz_animal(obter_animal(m, nova_pos))
                        inserir_animal(m, novo, pos_anterior)
    for linha in range(1, m["dimensao"][1]):
        for coluna in range(1, m["dimensao"][0]):
            if eh_posicao_animal(m, cria_posicao(coluna, linha)):
                if "check" in obter_animal(m, cria_posicao(coluna, linha)):
                    obter_animal(m, cria_posicao(coluna, linha)).pop("check")
                if eh_animal_faminto(obter_animal(m, cria_posicao(coluna, linha))):
                    eliminar_animal(m, cria_posicao(coluna, linha))
    return m


def score_aux(m):
    """score_aux: prado → str

    Esta função auxiliar recebe um prado e devolve uma string com o número de predadores e o número de presas, entre
    parênteses."""
    return ''.join("(" + str(obter_numero_predadores(m)) + ", " + str(obter_numero_presas(m)) + ")")


def simula_ecossistema(f, g, v):
    fich = open(f, "r")
    linhas = fich.readlines()
    linhas = ''.join(linhas)
    linhas = linhas.split("\n")
    dimensao = linhas[0].replace("(", "").replace(")", "")
    dimensao = dimensao.split(",")
    dimensao_f = ()
    for n in dimensao:
        dimensao_f += (int(n),)
    rochedos = linhas[1].replace("(", "").replace(")", "")
    if rochedos != "":
        rochedos = rochedos.split(",")
        rochedos_f = ()
        for i in range(0, len(rochedos), 2):
            rochedos_f += ((int(rochedos[i]), int(rochedos[i+1])),)
    else:
        rochedos_f = ()
    animais_pos = linhas[2:len(linhas)-1]
    for i in range(len(animais_pos)):
        animais_pos[i] = animais_pos[i].replace("(", "").replace(")", "").replace("'", "").replace('"', "")
    animais_f = ()
    pos_f = ()
    for animal in animais_pos:
        elementos = animal.split(",")
        especie = str(elementos[0])
        reprod = int(elementos[1])
        alimen = int(elementos[2])
        pos = (int(elementos[3]), int(elementos[4]),)
        pos_f += (pos,)
        animal_f = cria_animal(especie, reprod, alimen)
        animais_f += (animal_f,)
    prado = cria_prado(dimensao_f, rochedos_f, animais_f, pos_f)
    gen = 0
    i = 0
    if v is False:
        print("Predadores:", str(obter_numero_predadores(prado)), "vs Presas:", str(obter_numero_presas(prado)),
              "(Gen.", str(gen) + ")")
        print(prado_para_str(prado))
        while i < g:
            geracao(prado)
            i += 1
            gen += 1
        print("Predadores:", str(obter_numero_predadores(prado)), "vs Presas:", str(obter_numero_presas(prado)),
              "(Gen.", str(gen) + ")")
        print(prado_para_str(prado))
    else:
        print("Predadores:", str(obter_numero_predadores(prado)), "vs Presas:", str(obter_numero_presas(prado)),
              "(Gen." + str(gen) + ")")
        print(prado_para_str(prado))
        while i < g:
            antes_presas = obter_numero_presas(prado)
            antes_predadores = obter_numero_predadores(prado)
            geracao(prado)
            gen += 1
            depois_presas = obter_numero_presas(prado)
            depois_predadores = obter_numero_predadores(prado)
            if antes_presas != depois_presas or antes_predadores != depois_predadores:
                print("Predadores:", str(obter_numero_predadores(prado)), "vs Presas:", str(obter_numero_presas(prado)),
                      "(Gen.", str(gen) + ")")
                print(prado_para_str(prado))
            i += 1
    return "(" + str(obter_numero_predadores(prado)) + ", " + str(obter_numero_presas(prado)) + ")"