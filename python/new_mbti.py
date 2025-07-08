def mbti_test():
    
    print("Selamat datang di tes MBTI sederhana!")
    
    e_i = input("Apakah kamu lebih suka berbicara dengan banyak orang atau menikmati waktu sendiri? (True/False): ").strip().lower() == "true"
    
    e_i2 = input("Apakah kamu lebih suka berbicara langsung dengan orang baru daripada mengamati dari jauh? (True/False): ").strip().lower() == "true"
    
    e_i3 = input("Apakah kamu merasa bosan jika terlalu lama sendirian? (True/False): ").strip().lower() == "true"
    
    s_n = input("Apakah kamu lebih suka informasi konkret dan detail atau ide dan kemungkinan besar? (True/False): ").strip().lower() == "true"
    
    s_n2 = input("Apakah kamu lebih fokus pada detail daripada gambaran besar? (True/False): ").strip().lower() == "true"
    
    s_n3 = input("Apakah kamu merasa nyaman mengikuti instruksi langkah demi langkah? (True/False): ").strip().lower() == "true"
    
    t_f = input("Apakah kamu lebih suka membuat keputusan berdasarkan logika atau mempertimbangkan perasaan orang lain? (True/False): ").strip().lower() == "true"
    
    t_f2 = input("Apakah kamu merasa adil lebih penting daripada baik hati? (True/False): ").strip().lower() == "true"
    
    t_f3 = input("Apakah kamu sering dinilai terlalu objektif atau blak-blakan? (True/False): ").strip().lower() == "true"
    
    j_p = input("Apakah kamu lebih suka merencanakan segalanya atau lebih fleksibel dan spontan? (True/False): ").strip().lower() == "true"
    
    j_p2 = input("Apakah kamu merasa tidak nyaman jika segala sesuatunya tidak pasti? (True/False): ").strip().lower() == "true"
    
    j_p3 = input("Apakah kamu lebih memilih menyelesaikan tugas jauh sebelum tenggat waktu? (True/False): ").strip().lower() == "true"
    
    E_score = sum([e_i, e_i2, e_i3]) 
    S_score = sum([s_n, s_n2, s_n3])
    T_score = sum([t_f, t_f2, t_f3])
    J_score = sum([j_p, j_p2, j_p3])
    
    if E_score >= 2:
        e_i_letter = "E"
    else:
        e_i_letter = "I"
    
    if S_score >= 2:
        s_n_letter = "S"
    else:
        s_n_letter = "N"
        
    if T_score >= 2:
        t_f_letter = "T"
    else:
        t_f_letter = "F"
        
    if J_score >= 2:
        j_p_letter = "J"
    else:
        j_p_letter = "P"


    mbti_type = e_i_letter + s_n_letter + t_f_letter + j_p_letter
    

    print(f"\nTipe MBTI kamu adalah: {mbti_type}")

mbti_test()