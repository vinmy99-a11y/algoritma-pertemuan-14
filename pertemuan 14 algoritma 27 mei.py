def bubble_sort_nama(arr):
    n = len(arr)
   
    for i in range(n - 1):
        swapped = False
        
        for j in range(n - i - 1):
            
            if arr[j].lower() > arr[j + 1].lower():
                
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                
        if not swapped:
            break
    return arr

if __name__ == "__main__":
   
    peserta_lomba = ["Dewi", "Budi", "Andi", "Citra", "Eko", "Fani", "Gilang"]
    
    print("Daftar Peserta Asli :", peserta_lomba)
    
    nama_terurut = bubble_sort_nama(peserta_lomba)
    
    print("Daftar Peserta (Sesuai Abjad):", nama_terurut)