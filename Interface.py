from tkinter import Tk, ttk, StringVar, IntVar, messagebox
from Application import Connection


class Interface_App(Tk):
    def __init__(self):
        super().__init__()
        
        # user logado id
        self.ID_USER_LOGADO = None
        
        self.style = ttk.Style()
        self.style.theme_use('alt')

        # FRAME LOGIN BACKGROUND
        self.style.configure('Login.TFrame', background='white')
        # FRAME LOGADO BACKGROUND
        self.style.configure('Logado.TFrame', background='white')
        # FRAME INFORMAÇÕES BACKGROUND
        self.style.configure('Informacoes.TFrame', background='white')
        # FRAME CADASTRO BACKGROUND
        self.style.configure('Cadastro.TFrame', background='white')
        # FRAME AVALIAÇÃO BACKGROUND
        self.style.configure('Avaliacao.TFrame', background='white')
        # FRAME CIRCUNFERÊNCIAS BACKGROUND
        self.style.configure('Circunferencias.TFrame', background='white')
        # FRAME DOBRAS BACKGROUND
        self.style.configure('Dobras.TFrame', background='white')

        
        self.style.configure('R.TButton', background = 'red', foreground = 'white', width=10, borderwidth=1, focusthickness=3, focuscolor='none')
        
        self.style.configure('G.TButton', background = 'green', foreground = 'white', borderwidth=1, focusthickness=3, focuscolor='none')
        
        self.style.configure('O.TButton', background = 'orange', foreground = 'white', width=5, borderwidth=1, focusthickness=3, focuscolor='none')
        
        self.style.layout("EntryStyle.TEntry",
                   [('Entry.plain.field', {'children': [(
                       'Entry.background', {'children': [(
                           'Entry.padding', {'children': [(
                               'Entry.textarea', {'sticky': 'nswe'})],
                      'sticky': 'nswe'})], 'sticky': 'nswe'})],
                      'border':'2', 'sticky': 'nswe'})])

        self.style.configure("EntryStyle.TEntry",
                 background="#000", 
                 foreground="#f00",
                 fieldbackground="#DDD",
                 padding=1)
        
        # SET FRAMES STYLES
        self.login_frame = ttk.Frame(self, style='Login.TFrame')
        self.logado_frame = ttk.Frame(self, style='Logado.TFrame')
        self.informacoes_frame = ttk.Frame(self, style='Informacoes.TFrame')
        self.cadastro_frame = ttk.Frame(self, style='Cadastro.TFrame')
        self.avaliacao_frame = ttk.Frame(self, style='Avaliacao.TFrame')
        self.circunferencias_frame = ttk.Frame(self, style='Circunferencias.TFrame')
        self.dobras_frame = ttk.Frame(self, style='Dobras.TFrame')

        # WIDGETS ON AVALIACAO FRAME
        self.avaliacao_lbl= ttk.Label(self.avaliacao_frame, text='AVALIAÇÃO FÍSICA')
        self.avaliacao_lbl.configure(foreground='#00A', background='#FFF', anchor="center", font=('Times', 12, 'bold'))
        
        self.id_user_label = ttk.Label(self.avaliacao_frame, text='Id do Aluno:')
        self.id_user_label.configure(foreground='green', background='#FFF',anchor="center", font=('Times', 8, 'bold'))
        
        self.sexo_label = ttk.Label(self.avaliacao_frame, text='Sexo:')
        self.sexo_label.configure(foreground='green', background='#FFF',anchor="center", font=('Times', 8, 'bold'))
        
        self.altura_label = ttk.Label(self.avaliacao_frame, text='Altura:')
        self.altura_label.configure(foreground='green', background='#FFF',anchor="center", font=('Times', 8, 'bold'))
        
        self.peso_label = ttk.Label(self.avaliacao_frame, text='Peso:')
        self.peso_label.configure(foreground='green', background='#FFF',anchor="center", font=('Times', 8, 'bold'))
        
        self.fc_label = ttk.Label(self.avaliacao_frame, text='Freq. Cardíaca:')
        self.fc_label.configure(foreground='green', background='#FFF',anchor="center", font=('Times', 8, 'bold'))
        
        self.pa_label = ttk.Label(self.avaliacao_frame, text='Pressão Arterial:')
        self.pa_label.configure(foreground='green', background='#FFF',anchor="center", font=('Times', 8, 'bold'))
        
        self.id_user_v = StringVar()
        self.id_user_entry = ttk.Entry(self.avaliacao_frame, style="EntryStyle.TEntry", width=25, textvariable=self.id_user_v)
        
        self.sexo_entry_v = StringVar()
        self.sex_values =("Masculino", "Feminino")
        self.sexo_entry = ttk.Combobox(self.avaliacao_frame, values=self.sex_values,textvariable=self.sexo_entry_v, state='readonly')
        
        self.altura_entry_v = StringVar()
        self.altura_entry = ttk.Entry(self.avaliacao_frame, style="EntryStyle.TEntry", width=25, textvariable=self.altura_entry_v)
        
        self.peso_entry_v = StringVar()
        self.peso_entry = ttk.Entry(self.avaliacao_frame, style="EntryStyle.TEntry", width=25, textvariable=self.peso_entry_v)
        
        self.freq_card_entry_v = StringVar()
        self.freq_card_entry = ttk.Entry(self.avaliacao_frame, style="EntryStyle.TEntry", width=25, textvariable=self.freq_card_entry_v)
        
        self.press_art_entry_v = StringVar()
        self.press_art_entry= ttk.Entry(self.avaliacao_frame, style="EntryStyle.TEntry", width=25, textvariable=self.press_art_entry_v)
        
        self.voltar_tela_logado_avaliacao_btn = ttk.Button(self.avaliacao_frame, text='Voltar', style = 'G.TButton', command = self.tela_usuario_logado)
        self.salvar_avaliacao_btn = ttk.Button(self.avaliacao_frame, style='O.TButton', text="Salvar", command=self.salvar_avaliacao)

        # WIDGETS ON LOGIN FRAME
        self.title("Personal Trainer System")
        
        self.title_lbl = ttk.Label(self.login_frame, text="PERSONAL TRAINER SYSTEM")
        self.title_lbl.configure(foreground='#00A', background='#FFF', anchor="center", font=('Times', 12, 'bold'))
        
        self.login_lbl = ttk.Label(self.login_frame, text='LOGIN')
        self.login_lbl.configure(foreground='#00A', background='#FFF',anchor="center", font=('Times', 10, 'bold'))
        
        self.email_lbl = ttk.Label(self.login_frame, text='E-mail:')
        self.email_lbl.configure(background='#FFF',foreground='#00A', font=('Times', 8, 'bold'))

        self.password_lbl = ttk.Label(self.login_frame, text='Password:')
        self.password_lbl.configure(background='#FFF', foreground='#00A', font=('Times', 8, 'bold'))
        
        self.email_entry_v = StringVar()
        self.email_entry = ttk.Entry(self.login_frame, style="EntryStyle.TEntry", width=25, textvariable=self.email_entry_v)
        
        self.password_entry_v = StringVar()
        self.password_entry = ttk.Entry(self.login_frame, style="EntryStyle.TEntry", width=25, show='*', textvariable=self.password_entry_v)
        
        self.submit_btn = ttk.Button(self.login_frame, text='Submit', style='G.TButton', command=self.login_test)
        
        self.exit_btn = ttk.Button(self.login_frame, text='Exit', style = 'R.TButton', command = self.destroy)
            
        self.div_up = ttk.Separator(self.login_frame)
        self.div_center = ttk.Separator(self.login_frame)
        self.div_top = ttk.Separator(self.login_frame)
        self.div_bottom = ttk.Separator(self.login_frame)
        
        self.clear_email = ttk.Button(self.login_frame, text='Clear', style = 'O.TButton', command = self.clear_mail)
        self.clear_email.configure(width=5)
        
        self.clear_password = ttk.Button(self.login_frame, text='Clear', style = 'O.TButton', command = self.clear_pass)
        self.clear_password.configure(width=5)
        
        self.cadastrar_novo_lbl = ttk.Label(self.login_frame, text='Não é cadastrado? Cadastre-se:')
        self.cadastrar_novo_lbl.configure(background='#FFF', foreground='#B00', font=('Times', 6, 'bold'))
        
        self.cadastrar_btn = ttk.Button(self.login_frame, text='Ok', style = 'O.TButton', command = self.tela_de_cadastro)
        self.clear_password.configure(width=5)
        self.div_end = ttk.Separator(self.login_frame)
        
        # WIDGETS ON TELA LOGADO
        self.second_label = ttk.Label(self.logado_frame, text="Você está logado")
        
        self.second_label.configure(background='#FFF', foreground='#00F')
        
        self.erro_login_label = ttk.Label(self.logado_frame, text="ERRO: Usuário ou Senha Incorretos!")
        
        self.erro_login_label.configure(background='#FFF', foreground='#F00')
        self.cadastrar_avaliacao_btn = ttk.Button(self.logado_frame, style = 'G.TButton', text='Nova Avaliação', command=self.tela_avaliacao)
        self.mostra_info_btn = ttk.Button(self.logado_frame, style = 'G.TButton', text='Dados do Aluno', command=self.tela_mostra_info)
        
        # WIDGETS DA TELA MOSTRA INFO
        self.dados_aluno_label = ttk.Label(self.informacoes_frame, text='DADOS DO ALUNO')
        self.dados_aluno_label.configure(foreground='#00A', background='#FFF', anchor="center", font=('Times', 12, 'bold'))
        
        self.id_res_info_db = ""
        self.nome_info_db = ""
        self.telefone_info_db = ""
        self.email_info_db = ""
        self.nascimento_info_db = ""
        self.data_cadastro_info_db = ""

        # id info label
        self.id_info_label = ttk.Label(self.informacoes_frame, text='Id:')
        self.id_info_label.configure(background='#FFF', foreground='#00A', font=('Times', 8, 'bold'),anchor="center")
        # id resultado
        self.id_res_lbl = ttk.Label(self.informacoes_frame, text=str(self.id_res_info_db))
        self.id_res_lbl.configure(background='#FFF', foreground='#A00', font=('Times', 8, 'bold'),anchor="center")
            
        # nome info label
        self.nome_info_label = ttk.Label(self.informacoes_frame, text='Nome:')
        self.nome_info_label.configure(background='#FFF', foreground='#00A', font=('Times', 8, 'bold'),anchor="center")
        # nome resultado
        self.nome_res_lbl = ttk.Label(self.informacoes_frame, text=self.nome_info_db)
        self.nome_res_lbl.configure(background='#FFF', foreground='#A00', font=('Times', 8, 'bold'),anchor="center")
            
        # telefone info label
        self.telefone_info_label = ttk.Label(self.informacoes_frame, text='Telefone:')
        self.telefone_info_label.configure(background='#FFF', foreground='#00A', font=('Times', 8, 'bold'),anchor="center")
        # telefone resultado
        self.telefone_res_lbl = ttk.Label(self.informacoes_frame, text=self.telefone_info_db)
        self.telefone_res_lbl.configure(background='#FFF', foreground='#A00', font=('Times', 8, 'bold'),anchor="center")
            
        # email info label
        self.email_info_label = ttk.Label(self.informacoes_frame, text='E-mail:')
        self.email_info_label.configure(background='#FFF', foreground='#00A', font=('Times', 8, 'bold'),anchor="center")
        # email resultado
        self.email_res_lbl = ttk.Label(self.informacoes_frame, text=self.email_info_db)
        self.email_res_lbl.configure(background='#FFF', foreground='#A00', font=('Times', 8, 'bold'),anchor="center")
            
        # nascimento info label
        self.nascimento_info_label = ttk.Label(self.informacoes_frame, text='Nascimento:')
        self.nascimento_info_label.configure(background='#FFF', foreground='#00A', font=('Times', 8, 'bold'),anchor="center")
        # nascimento resultado
        self.nascimento_res_lbl = ttk.Label(self.informacoes_frame, text=self.nascimento_info_db)
        self.nascimento_res_lbl.configure(background='#FFF', foreground='#A00', font=('Times', 8, 'bold'),anchor="center")
            
        # data cadastro info label
        self.data_cadastro_info_label = ttk.Label(self.informacoes_frame, text='Cadastrado em:')
        self.data_cadastro_info_label.configure(background='#FFF', foreground='#00A', font=('Times', 8, 'bold'),anchor="center")
        # data cadastro resultado
        self.data_cadastro_res_lbl = ttk.Label(self.informacoes_frame, text=self.data_cadastro_info_db)
        self.data_cadastro_res_lbl.configure(background='#FFF', foreground='#A00', font=('Times', 8, 'bold'),anchor="center")

        self.voltar_tela_logado_btn = ttk.Button(self.informacoes_frame, style = 'G.TButton', text="Voltar", command=self.tela_usuario_logado)

        # WIDGETS DA TELA DE CADASTRO
        self.nome_cadastro_label = ttk.Label(self.cadastro_frame, text='Nome:')
        self.nome_cadastro_label.configure(background='#FFF', foreground='#00A')
        
        self.nome_cadastro_entry_v = StringVar()
        self.nome_cadastro_entry = ttk.Entry(self.cadastro_frame, style="EntryStyle.TEntry", width=25, textvariable=self.nome_cadastro_entry_v)
        
        self.telefone_cadastro_label = ttk.Label(self.cadastro_frame, text='Telefone:')
        self.telefone_cadastro_label.configure(background='#FFF', foreground='#00A')
        
        self.telefone_cadastro_entry_v = StringVar()
        self.telefone_cadastro_entry = ttk.Entry(self.cadastro_frame, style="EntryStyle.TEntry", width=25, textvariable=self.telefone_cadastro_entry_v)
        
        self.nascimento_cadastro_label = ttk.Label(self.cadastro_frame, text='Nascimento:')
        self.nascimento_cadastro_label.configure(background='#FFF', foreground='#00A')
        
        self.nascimento_cadastro_entry_v = StringVar()
        self.nascimento_cadastro_entry = ttk.Entry(self.cadastro_frame, style="EntryStyle.TEntry", width=25, textvariable=self.nascimento_cadastro_entry_v)
        
        self.email_cadastro_label = ttk.Label(self.cadastro_frame, text='E-mail:')
        self.email_cadastro_label.configure(background='#FFF', foreground='#00A')
        
        self.email_cadastro_entry_v = StringVar()
        self.email_cadastro_entry = ttk.Entry(self.cadastro_frame, style="EntryStyle.TEntry", width=25, textvariable=self.email_cadastro_entry_v)
        
        self.senha_cadastro_label = ttk.Label(self.cadastro_frame, text='Senha:')
        self.senha_cadastro_label.configure(background='#FFF', foreground='#00A')
        
        self.senha_cadastro_entry_v = StringVar()
        self.senha_cadastro_entry = ttk.Entry(self.cadastro_frame, style="EntryStyle.TEntry", width=25, textvariable=self.senha_cadastro_entry_v)
        
        self.inserir_dados_cadastro_btn = ttk.Button(self.cadastro_frame, style = 'G.TButton', text='Cadastrar', command=self.inserir_dados_cadastro)
        
        self.login_screen()

    def back(self):
        self.dobras_frame.grid_remove()
        self.tela_avaliacao()
    
    def fechar(self):
        self.avaliacao_frame.grid_remove()
        self.dobras_frame.grid_remove()
        self.destroy()

    # AQUI DEFINIMOS A TELA DE LOGIN
    def login_screen(self):
        self.limpa_frames()

        self.configure(bg='#FFF')
        self.login_frame.grid()

        self.div_up.grid(row=0, column=0, columnspan=3, sticky='we', padx=10, pady=20)
        
        self.title_lbl.grid(row=1, column=0, columnspan=3, sticky='nswe', padx=10, pady=20)
        
        self.login_lbl.grid(row=3, column=0, columnspan=3, sticky='nswe', padx=10, pady=20)
        
        self.div_top.grid(row=2, column=0, columnspan=3, sticky='we', padx=10, pady=20)
        
        self.email_lbl.grid(row=4, column=0, sticky="ew", padx=10, pady=20, ipady=15)
        
        self.password_lbl.grid(row=5, column=0, sticky="ew", padx=10, pady=20, ipady=15)
        
        self.email_entry.grid(row=4, column=1, sticky='we', padx=10, pady=20, ipady=15)
        
        self.password_entry.grid(row=5, column=1, sticky='we', padx=10, pady=20, ipady=15)
        
        self.div_center.grid(row=6, column=0, columnspan=3, sticky='we', padx=10, pady=20)
        
        self.submit_btn.grid(row=7, column=1, columnspan=2, sticky="ew", padx=10, pady=20, ipady=20)
        
        self.exit_btn.grid(row=7, column=0, sticky="ew", padx=10, pady=20, ipady=20)
        
        self.div_bottom.grid(row=8, column=0, columnspan=3, sticky='we', padx=10, pady=20)
        
        self.clear_email.grid(row=4, column=2, columnspan=1, sticky='e', padx=10, pady=10, ipady=15)
        
        self.clear_password.grid(row=5, column=2, columnspan=1, sticky='e', padx=10, pady=10, ipady=15)
        
        self.cadastrar_novo_lbl.grid(row=9, column=1, columnspan=2, sticky="we", padx=10, pady=10, ipady=10)
        
        self.cadastrar_btn.grid(row=9, column=2,columnspan=1, sticky="we", padx=10, pady=10, ipady=15)
        
        self.div_end.grid(row=10, column=0, columnspan=3, sticky='we', padx=10, pady=20)

    # LIMPA OS FRAMES
    def limpa_frames(self):
        lista = [self.login_frame, self.logado_frame,
                 self.cadastro_frame, self.avaliacao_frame,
                 self.circunferencias_frame, self.dobras_frame,
                 self.informacoes_frame]
        for frame in lista:
            frame.grid_remove()
    
    # TESTA EMAIL E SENHA
    def login_test(self):
        c = Connection('personal_database.db')
        if c.usuario_autenticado(self.email_entry.get().strip().lower(), self.password_entry.get()):
            self.ID_USER_LOGADO = c.user_id()
            self.tela_usuario_logado()
            c.close_db()
            messagebox.showinfo(title='Sucesso', message='Logado com sucesso!')
        else:
            self.tela_erro_login()
            c.close_db()
            return False

    #CHAMA SE O LOGIN DER ERRO 
    def tela_erro_login(self):
        self.limpa_frames()
        self.erro_login_label.grid(row=0, column=0, padx=10, pady=10)

    # CHAMA SE O LOGIN FOI BEM SUCEDIDO
    def tela_usuario_logado(self):
        self.limpa_frames()
        # Here is placed the secondo screen widgets
        self.logado_frame.grid()
        #self.second_label.grid(row=0, column=0, padx=10, pady=10)
        self.cadastrar_avaliacao_btn.grid(row=1, column=0, sticky='we', padx=10, pady=10, ipady=20)
        self.mostra_info_btn.grid(row=2, column=0, sticky='we', padx=10, pady=10, ipady=20)
    
    # TELA COM AS INFORMACÕES DO USER
    def tela_mostra_info(self):
        self.limpa_frames()
        self.configure(bg='#FFF')
        self.informacoes_frame.grid()
        # Conexão
        c = Connection('personal_database.db')
        self.dados_info = c.select_by_id(int(self.ID_USER_LOGADO))
        c.close_db()
        # Título
        self.dados_aluno_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10, ipady=15, sticky='we')
        # Info Labels
        self.id_info_label.grid(row=1, column=0, padx=10, pady=10, ipady=15, sticky='we')
        self.nome_info_label.grid(row=2, column=0, padx=10, pady=10, ipady=15, sticky='we')
        self.telefone_info_label.grid(row=3, column=0, padx=10, pady=10, ipady=15, sticky='we')
        self.email_info_label.grid(row=4, column=0, padx=10, pady=10, ipady=15, sticky='we')
        self.nascimento_info_label.grid(row=5, column=0, padx=10, pady=10, ipady=15, sticky='we')
        self.data_cadastro_info_label.grid(row=6, column=0, padx=10, pady=10, ipady=15, sticky='we')
        # DB Res Label
        self.id_res_lbl['text'] = self.dados_info[0][0]
        self.id_res_lbl.grid(row=1, column=1, padx=10, pady=10, ipady=15, sticky='we')
        self.nome_res_lbl['text'] = self.dados_info[0][1].title()
        self.nome_res_lbl.grid(row=2, column=1, padx=10, pady=10, ipady=15, sticky='we')
        self.telefone_res_lbl['text'] = self.dados_info[0][2]
        self.telefone_res_lbl.grid(row=3, column=1, padx=10, pady=10, ipady=15, sticky='we')
        self.email_res_lbl['text'] = self.dados_info[0][4]
        self.email_res_lbl.grid(row=4, column=1, padx=10, pady=10, ipady=15, sticky='we')
        self.nascimento_res_lbl['text'] = self.dados_info[0][3]
        self.nascimento_res_lbl.grid(row=5,column=1, padx=10, pady=10, ipady=15, sticky='we')
        self.data_cadastro_res_lbl['text'] = self.dados_info[0][7][:11]
        self.data_cadastro_res_lbl.grid(row=6, column=1, padx=10, pady=10, ipady=15, sticky='we')
        self.voltar_tela_logado_btn.grid(row=7, column=0, columnspan=2, padx=10, pady=10, ipady=15, sticky='we')

   # TELA DE CADASTRO 
    def tela_de_cadastro(self):
        self.limpa_frames()
        # BACKGROUND
        self.configure(bg='#FFF')
        self.cadastro_frame.grid()
        # Aqui setamos os widgets na tela
        self.nome_cadastro_label.grid(row=0, column=0, padx=10, pady=10, ipady=15)
        self.nome_cadastro_entry.grid(row=0, column=1, padx=10, pady=10, ipady=15)
        self.telefone_cadastro_label.grid(row=1, column=0, padx=10, pady=10, ipady=15)
        self.telefone_cadastro_entry.grid(row=1, column=1, padx=10, pady=10, ipady=15)
        self.nascimento_cadastro_label.grid(row=2, column=0, padx=10, pady=10, ipady=15)
        self.nascimento_cadastro_entry.grid(row=2, column=1, padx=10, pady=10, ipady=15)
        self.email_cadastro_label.grid(row=3, column=0, padx=10, pady=10, ipady=15)
        self.email_cadastro_entry.grid(row=3 , column=1, padx=10, pady=10, ipady=15)
        self.senha_cadastro_label.grid(row=4, column=0, padx=10, pady=10, ipady=15)
        self.senha_cadastro_entry.grid(row=4, column=1, padx=10, pady=10, ipady=15)
        self.inserir_dados_cadastro_btn.grid(row=7, column=1, sticky='we', padx=10, pady=10, ipady=20)

    # TELA DE AVALIAÇÂO
    def tela_avaliacao(self):
        self.limpa_frames()
        # BACKGROUND
        self.configure(bg='#FFF')
        self.avaliacao_frame.grid()
        # widgets
        self.avaliacao_lbl.grid(row=0, column=0, padx=10, pady=10, ipadx=15, ipady=15, sticky='we', columnspan=2)
        self.sexo_label.grid(row=2, column=0, padx=10, pady=30, ipady=15, sticky='w')
        self.sexo_entry.grid(row=2, column=1, padx=10, pady=20, ipady=15, sticky='we')
        self.altura_label.grid(row=3, column=0, padx=10, pady=20, ipady=15, sticky='w')
        self.altura_entry.grid(row=3, column=1, padx=10, pady=20, ipady=15, sticky='we')
        self.peso_label.grid(row=4, column=0, padx=10, pady=20, ipady=15, sticky='w')
        self.peso_entry.grid(row=4, column=1, padx=10, pady=20, ipady=15, sticky='we')
        self.fc_label.grid(row=5, column=0, padx=10, pady=20, ipady=15, sticky='w')
        self.freq_card_entry.grid(row=5, column=1, padx=10, pady=20, ipady=15, sticky='we')
        self.pa_label.grid(row=6, column=0, padx=10, pady=20, ipady=15, sticky='w')
        self.press_art_entry.grid(row=6, column=1, padx=10, pady=20, ipady=15, sticky='we')
        self.salvar_avaliacao_btn.grid(row=10, column=1, padx=10, pady=10, ipadx=15, ipady=15, sticky='we')
        self.voltar_tela_logado_avaliacao_btn.grid(row=10, column=0, padx=10, pady=10, ipadx=15, ipady=15, sticky='w')
        
    def tela_dobras(self):
        self.limpa_frames()
        # BACKGROUND
        self.configure(bg='#FFF')
        self.dobras_frame.grid()
        self.tela_dobras_lbl.grid(row=0, column=0)
        self.back_tela_dobras.grid(row=1, column=0)
        self.exit_tela_dobras.grid(row=2, column=0)
        
    def salvar_avaliacao(self):
        c = Connection('personal_database.db')
        id_aluno = self.ID_USER_LOGADO
        #id_aluno = int(self.id_user_entry.get())
        sexo_aluno = str(self.sexo_entry.get())
        altura_aluno = float(self.altura_entry.get())
        peso_aluno = float(self.peso_entry.get())
        fc_aluno = int(self.freq_card_entry.get())
        pa_aluno = str(self.press_art_entry.get())
        if c.cadastra_avaliacao(id_aluno, sexo_aluno, altura_aluno, peso_aluno , fc_aluno, pa_aluno):
            # Se Sucesso
            messagebox.showinfo(title='Sucesso', message='Avaliação cadastrada com sucesso!')
            # Fecha a conexão com o DB
            c.close_db()
            self.tela_usuario_logado()
        else:
            # Se der Erro
            messagebox.showwarning(title='Erro', message='ERRO!')

    def voltar_tela_login(self):
        self.login_screen()
    
    def clear_pass(self):
        self.password_entry.delete(0, 'end')
    
    def clear_mail(self):
        self.email_entry.delete(0, 'end')
    
    # DEFINIR OS MÉTODOS PARA CADASTRAR
    def inserir_dados_cadastro(self):
        nome = self.nome_cadastro_entry.get().lower().strip()
        telefone = self.telefone_cadastro_entry.get().strip()
        nascimento = self.nascimento_cadastro_entry.get()
        email = self.email_cadastro_entry.get().lower().strip()
        senha = self.senha_cadastro_entry.get()
        # Conecta ao DB
        c = Connection('personal_database.db')
        # Cadastra os dados
        if c.cadastra_aluno(nome, telefone, nascimento, email, senha, 0):
            # Se Sucesso
            messagebox.showinfo(title='Sucesso', message='Dados cadastrados com sucesso!')
            # Fecha a conexão com o DB
            c.close_db()
            #self.limpa_tela()
            self.login_screen()
        else:
            # Se der Erro
            messagebox.showwarning(title='Erro', message='ERRO!')
        

if __name__ == "__main__":
    app = Interface_App()
    app.mainloop()
