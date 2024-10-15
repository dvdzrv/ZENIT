moj_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer et diam ac elit mollis varius sit amet sed ante. In et nunc metus. Donec scelerisque eu diam nec fermentum. Praesent sit amet accumsan risus. Aliquam vel commodo dui, quis tempor massa. Curabitur tellus augue, facilisis non laoreet eu, commodo sit amet nulla. Vivamus neque sapien, maximus nec purus vel, mattis finibus tortor. Morbi convallis mauris nibh. Sed sed sodales diam. Etiam dapibus tincidunt diam quis ultricies. "


diakritika = ['ľ', 'š', 'č', 'ť', 'ž', 'ý', 'á', 'í', 'é', 'ú', 'ä', 'ô', 'ň']
bez_diakritiky = ['l', 's', 'c', 't', 'z', 'y', 'a', 'i', 'e', 'u', 'a', 'o', 'n']

#ODSTRANENIE ZNAKOV
bez_bodiek = moj_text.replace('.', '')


#VYMENA ZNAKOV
for i in range(len(diakritika)):    
    txt_bez_diakritiky = moj_text.replace(diakritika[i], bez_diakritiky[i])


#NAJDENIE NAJDLHIEHO SLOVA
pocet_znakov = 0
for i in range(len(moj_text)):
    if len(moj_text[i]) > pocet_znakov:
        slovo = moj_text[i]
        pocet_znakov = len(moj_text[i])
