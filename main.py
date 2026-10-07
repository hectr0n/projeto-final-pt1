import discord
from discord.ext import commands
import random
import asyncio

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


# ================= READY =================

@bot.event
async def on_ready():
    print("Bot ligado como", bot.user)


# ================= COMANDOS =================

@bot.command()
async def oi(ctx):
    await ctx.send("Olá!")


@bot.command()
async def adoro(ctx):
    await ctx.send("Fico muito feliz com isso :)")


@bot.command()
async def mostrar(ctx):

    await ctx.send("pronto!")

    # ================= BROCK =================

    onix = {"vida": 300, "ataque": 110, "nome": "onix"}
    golem = {"vida": 350, "ataque": 110, "nome": "golem"}
    rydon = {"vida": 400, "ataque": 90, "nome": "rydon"}
    probopass = {"vida": 310, "ataque": 120, "nome": "probopass"}
    aggron = {"vida": 370, "ataque": 95, "nome": "aggron"}

    brock = [aggron, probopass, rydon, onix, golem]

    # ================= JOGADOR =================

    me = []

    # ================= SAMANTHA =================

    absol = {"vida": 300, "ataque": 170, "nome": "absol"}
    toxtricity = {"vida": 200, "ataque": 195, "nome": "toxtricity"}
    gallade = {"vida": 290, "ataque": 115, "nome": "gallade"}
    chandelure = {"vida": 275, "ataque": 135, "nome": "chandelure"}
    golisopod = {"vida": 380, "ataque": 100, "nome": "golisopod"}

    samantha = [
        toxtricity,
        absol,
        gallade,
        chandelure,
        golisopod
    ]

    trainer = []
    formacao = False

    # ================= PRIMEIRA OPÇÃO =================

    lucario = {
        "nome": "lucario",
        "vida": 300,
        "ataque": 150
    }

    charizard = {
        "nome": "charizard",
        "vida": 280,
        "ataque": 160
    }

    infernape = {
        "nome": "infernape",
        "vida": 290,
        "ataque": 155
    }

    venomsaur = {
        "nome": "venomsaur",
        "vida": 310,
        "ataque": 140
    }

    blastoise = {
        "nome": "blastoise",
        "vida": 320,
        "ataque": 135
    }

    # ================= SEGUNDA OPÇÃO =================

    garchomp = {
        "nome": "garchomp",
        "vida": 350,
        "ataque": 130
    }

    tyranitar = {
        "nome": "tyranitar",
        "vida": 200,
        "ataque": 195
    }

    gyarados = {
        "nome": "gyarados",
        "vida": 290,
        "ataque": 140
    }

    gengar = {
        "nome": "gengar",
        "vida": 275,
        "ataque": 155
    }

    scizor = {
        "nome": "scizor",
        "vida": 280,
        "ataque": 150
    }

    # ================= TERCEIRA OPÇÃO =================

    greninja = {
        "nome": "greninja",
        "vida": 270,
        "ataque": 160
    }

    incineroar = {
        "nome": "incineroar",
        "vida": 280,
        "ataque": 165
    }

    centiskorch = {
        "nome": "centiskorch",
        "vida": 250,
        "ataque": 185
    }

    machamp = {
        "nome": "machamp",
        "vida": 320,
        "ataque": 165
    }

    nidoking = {
        "nome": "nidoking",
        "vida": 270,
        "ataque": 175
    }

    # ================= QUARTA OPÇÃO =================

    raichu = {
        "nome": "raichu",
        "vida": 250,
        "ataque": 180
    }

    duraludon = {
        "nome": "duraludon",
        "vida": 270,
        "ataque": 170
    }

    umbreon = {
        "nome": "umbreon",
        "vida": 240,
        "ataque": 175
    }

    glaceon = {
        "nome": "glaceon",
        "vida": 240,
        "ataque": 175
    }

    dragonite = {
        "nome": "dragonite",
        "vida": 280,
        "ataque": 173
    }

    # ================= QUINTA OPÇÃO =================

    heracross = {
        "nome": "heracross",
        "vida": 300,
        "ataque": 150
    }

    mimikyu = {
        "nome": "mimikyu",
        "vida": 250,
        "ataque": 170
    }

    metagross = {
        "nome": "metagross",
        "vida": 275,
        "ataque": 172
    }

    pidgeot = {
        "nome": "pidgeot",
        "vida": 305,
        "ataque": 148
    }

    zoroark = {
        "nome": "zoroark",
        "vida": 315,
        "ataque": 140
    }

    zeraora = {
        "nome": "zeraora",
        "vida": 310,
        "ataque": 145
    }


    # ================= CHECK =================

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel


    # ==================================================
    # PRIMEIRA ESCOLHA
    # =============================================

    await ctx.send("Escolha seu primeiro pokémon:")
    await ctx.send(lucario)
    await asyncio.sleep(0.2)
    await ctx.send(charizard)
    await asyncio.sleep(0.2)
    await ctx.send(infernape)
    await asyncio.sleep(0.2)
    await ctx.send(venomsaur)
    await asyncio.sleep(0.2)
    await ctx.send(blastoise)

    msg1 = await bot.wait_for("message", check=check)
    escolha1 = msg1.content.lower()

    if escolha1 == "lucario":
        me.append(lucario)
        await ctx.send("Seu Lucario virou seu parceiro!")
        await ctx.send(lucario)

    elif escolha1 == "charizard":
        me.append(charizard)
        await ctx.send("Seu Charizard virou seu parceiro!")
        await ctx.send(charizard)

    elif escolha1 == "infernape":
        me.append(infernape)
        await ctx.send("Seu Infernape virou seu parceiro!")
        await ctx.send(infernape)

    elif escolha1 == "venomsaur":
        me.append(venomsaur)
        await ctx.send("Seu Venomsaur virou seu parceiro!")
        await ctx.send(venomsaur)

    elif escolha1 == "blastoise":
        me.append(blastoise)
        await ctx.send("Seu Blastoise virou seu parceiro!")
        await ctx.send(blastoise)

    else:
        await ctx.send("Esse pokémon não existe ou o nome foi digitado errado.")
        return


    # ============================================
    # SEGUNDA ESCOLHA
    # ==================================================

    await asyncio.sleep(0.5)

    await ctx.send("Escolha seu segundo pokémon:")
    await ctx.send(garchomp)
    await asyncio.sleep(0.2)
    await ctx.send(tyranitar)
    await asyncio.sleep(0.2)
    await ctx.send(gyarados)
    await asyncio.sleep(0.2)
    await ctx.send(gengar)
    await asyncio.sleep(0.2)
    await ctx.send(scizor)

    msg2 = await bot.wait_for("message", check=check)
    escolha2 = msg2.content.lower()

    if escolha2 == "garchomp":
        me.append(garchomp)
        await ctx.send("Garchomp entrou no seu time!")
        await ctx.send(garchomp)

    elif escolha2 == "tyranitar":
        me.append(tyranitar)
        await ctx.send("Tyranitar entrou no seu time!")
        await ctx.send(tyranitar)

    elif escolha2 == "gyarados":
        me.append(gyarados)
        await ctx.send("Gyarados entrou no seu time!")
        await ctx.send(gyarados)

    elif escolha2 == "gengar":
        me.append(gengar)
        await ctx.send("Gengar entrou no seu time!")
        await ctx.send(gengar)

    elif escolha2 == "scizor":
        me.append(scizor)
        await ctx.send("Scizor entrou no seu time!")
        await ctx.send(scizor)

    else:
        await ctx.send("Esse pokémon não existe ou o nome foi digitado errado.")
        return


    # ==================================================
    # TERCEIRA ESCOLHA
    # ==============================================

    await asyncio.sleep(0.5)

    await ctx.send("Escolha seu terceiro pokémon:")
    await ctx.send(greninja)
    await asyncio.sleep(0.2)
    await ctx.send(incineroar)
    await asyncio.sleep(0.2)
    await ctx.send(centiskorch)
    await asyncio.sleep(0.2)
    await ctx.send(machamp)
    await asyncio.sleep(0.2)
    await ctx.send(nidoking)

    msg3 = await bot.wait_for("message", check=check)
    escolha3 = msg3.content.lower()

    if escolha3 == "greninja":
        me.append(greninja)
        await ctx.send("Greninja entrou no seu time!")
        await ctx.send(greninja)

    elif escolha3 == "incineroar":
        me.append(incineroar)
        await ctx.send("Incineroar entrou no seu time!")
        await ctx.send(incineroar)

    elif escolha3 == "centiskorch":
        me.append(centiskorch)
        await ctx.send("Centiskorch entrou no seu time!")
        await ctx.send(centiskorch)

    elif escolha3 == "machamp":
        me.append(machamp)
        await ctx.send("Machamp entrou no seu time!")
        await ctx.send(machamp)

    elif escolha3 == "nidoking":
        me.append(nidoking)
        await ctx.send("Nidoking entrou no seu time!")
        await ctx.send(nidoking)

    else:
        await ctx.send("Esse pokémon não existe ou o nome foi digitado errado.")
        return


    # ============================================
    # QUARTA ESCOLHA
    # ==================================================

    await asyncio.sleep(0.5)

    await ctx.send("Escolha seu quarto pokémon:")
    await ctx.send(raichu)
    await asyncio.sleep(0.2)
    await ctx.send(duraludon)
    await asyncio.sleep(0.2)
    await ctx.send(umbreon)
    await asyncio.sleep(0.2)
    await ctx.send(glaceon)
    await asyncio.sleep(0.2)
    await ctx.send(dragonite)

    msg4 = await bot.wait_for("message", check=check)
    escolha4 = msg4.content.lower()

    if escolha4 == "raichu":
        me.append(raichu)
        await ctx.send("Raichu entrou no seu time!")
        await ctx.send(raichu)

    elif escolha4 == "duraludon":
        me.append(duraludon)
        await ctx.send("Duraludon entrou no seu time!")
        await ctx.send(duraludon)

    elif escolha4 == "umbreon":
        me.append(umbreon)
        await ctx.send("Umbreon entrou no seu time!")
        await ctx.send(umbreon)

    elif escolha4 == "glaceon":
        me.append(glaceon)
        await ctx.send("Glaceon entrou no seu time!")
        await ctx.send(glaceon)

    elif escolha4 == "dragonite":
        me.append(dragonite)
        await ctx.send("Dragonite entrou no seu time!")
        await ctx.send(dragonite)

    else:
        await ctx.send("Esse pokémon não existe ou o nome foi digitado errado.")
        return


    # ==================================================
    # QUINTA ESCOLHA
    # ===============================================

    await asyncio.sleep(0.5)

    await ctx.send("Escolha seu quinto e último pokémon:")
    await ctx.send(heracross)
    await asyncio.sleep(0.2)
    await ctx.send(mimikyu)
    await asyncio.sleep(0.2)
    await ctx.send(metagross)
    await asyncio.sleep(0.2)
    await ctx.send(pidgeot)
    await asyncio.sleep(0.2)
    await ctx.send(zoroark)
    await asyncio.sleep(0.2)
    await ctx.send(zeraora)

    msg5 = await bot.wait_for("message", check=check)
    escolha5 = msg5.content.lower()

    if escolha5 == "heracross":
        me.append(heracross)
        await ctx.send("Heracross entrou no seu time!")
        await ctx.send(heracross)

    elif escolha5 == "mimikyu":
        me.append(mimikyu)
        await ctx.send("Mimikyu entrou no seu time!")
        await ctx.send(mimikyu)

    elif escolha5 == "metagross":
        me.append(metagross)
        await ctx.send("Metagross entrou no seu time!")
        await ctx.send(metagross)

    elif escolha5 == "pidgeot":
        me.append(pidgeot)
        await ctx.send("Pidgeot entrou no seu time!")
        await ctx.send(pidgeot)

    elif escolha5 == "zoroark":
        me.append(zoroark)
        await ctx.send("Zoroark entrou no seu time!")
        await ctx.send(zoroark)

    elif escolha5 == "zeraora":
        me.append(zeraora)
        await ctx.send("Zeraora entrou no seu time!")
        await ctx.send(zeraora)

    else:
        await ctx.send("Esse pokémon não existe ou o nome foi digitado errado.")
        return


    # ============================================
    # INÍCIO DA BATALHA
    # ==================================================

    await ctx.send("*" * 10 + " O jogo de Batalhas Pokémon " + "*" * 10)

    await ctx.send("Seu time está completo!")

    await ctx.send("Entre estes treinadores, qual você decide batalhar?")
    await ctx.send("1 - Brock")
    await asyncio.sleep(0.3)
    await ctx.send("2 - Samantha")
    await asyncio.sleep(0.3)
    await ctx.send("3 - Escolha aleatória")

    msg = await bot.wait_for("message", check=check)
    batalha = msg.content.lower()


    # =========================================
    # ESCOLHA DO TREINADOR
    # ==================================================

    if batalha == "1" or batalha == "brock":

        trainer = brock.copy()
        nome_trainer = "Brock"
        formacao = True

    elif batalha == "2" or batalha == "samantha":

        trainer = samantha.copy()
        nome_trainer = "Samantha"
        formacao = True

    elif batalha == "3" or batalha == "escolha aleatória" or batalha == "aleatoria":

        nome_trainer = random.choice(["Brock", "Samantha"])

        if nome_trainer == "Brock":
            trainer = brock.copy()
        else:
            trainer = samantha.copy()

        formacao = True

    else:

        await ctx.send("Desculpe, esse treinador não existe.")
        return


    await ctx.send("Que comece a batalha contra " + nome_trainer + "!!!!!!!")

    await asyncio.sleep(1)


    # ==================================================
    # BATALHA
    # ======================================

    while True:

        if len(me) == 0:

            await ctx.send("Você perdeu todos os seus pokémons.")
            break


        if len(trainer) == 0:

            await ctx.send(
                "Todos os pokémons do adversário foram derrotados. "
                "Você venceu!"
            )

            break


        await ctx.send("Seus pokémons:")

        for p in me:

            await ctx.send(
                p["nome"]
                + " | vida: "
                + str(p["vida"])
                + " | ataque: "
                + str(p["ataque"])
            )


        await ctx.send("Digite o nome do pokémon que você quer usar:")

        msg = await bot.wait_for("message", check=check)

        escolha = msg.content.lower()


        poke = None

        for p in me:

            if p["nome"] == escolha:

                poke = p
                break


        if poke is None:

            await ctx.send("Pokémon inválido, tente novamente.")
            continue


        oponente = random.choice(trainer)

        await ctx.send(
            nome_trainer
            + " escolheu: "
            + oponente["nome"]
        )


        # ==================================================
        # COMBATE
        # ============================================

        while poke["vida"] > 0 and oponente["vida"] > 0:

            await asyncio.sleep(1)

            await ctx.send(
                poke["nome"] + " atacou!"
            )

            oponente["vida"] -= poke["ataque"]


            if oponente["vida"] <= 0:

                await ctx.send(
                    "Você derrotou "
                    + oponente["nome"]
                    + "!"
                )

                trainer.remove(oponente)

                break


            else:

                await ctx.send(
                    oponente["nome"]
                    + " ficou com "
                    + str(oponente["vida"])
                    + " de vida."
                )


            await asyncio.sleep(1)

            await ctx.send("O adversário atacou!")

            poke["vida"] -= oponente["ataque"]


            if poke["vida"] <= 0:

                await ctx.send(
                    poke["nome"]
                    + " foi derrotado!"
                )

                me.remove(poke)

                break


            else:

                await ctx.send(
                    poke["nome"]
                    + " ficou com "
                    + str(poke["vida"])
                    + " de vida."
                )


# ================= TOKEN =================

bot.run("token_aqui")

# Todos os créditos a Heitor :)