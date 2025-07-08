def mbti_test():
    
    print("Welcome di tes mbti kecil dari kal")
    
    e_i = input("Apakah kamu lebih suka (E) berbicara dengan banyak orang atau (I) menikmati waktu sendiri? (E/I): ").strip().upper()
    
    s_n = input("Apakah kamu lebih suka (S) informasi konkret dan detail atau (N) ide dan kemungkinan besar? (S/N): ").strip().upper()
    
    t_f = input("Apakah kamu lebih suka (T) membuat keputusan berdasarkan logika atau (F) mempertimbangkan perasaan orang lain? (T/F): ").strip().upper()
    
    j_p = input("Apakah kamu lebih suka (J) merencanakan segalanya atau (P) lebih fleksibel dan spontan? (J/P): ").strip().upper()
    

    mbti_type = e_i + s_n + t_f + j_p
    

    print(f"\nTipe MBTI kamu adalah: {mbti_type}")

mbti_test()
