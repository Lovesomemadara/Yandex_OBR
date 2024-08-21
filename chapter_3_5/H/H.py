fir_file: str = input()
sec_file: str = input()
ans_file: str = input()

with (open(fir_file, mode='r', encoding='UTF-8') as fir,
      open(sec_file, mode='r', encoding='UTF-8') as sec):
    fir_items: set[str] = set([item for item in fir.read().split()])
    sec_items: set[str] = set([item for item in sec.read().split()])

unique: set[str] = fir_items ^ sec_items

with open(ans_file, mode='w', encoding='UTF-8') as ans:
    print('\n'.join(sorted(unique)), file=ans)
