# test40su.txt 파일을 한 행씩 읽어  각 행의 숫자의 합을 출력하시오

try:
    with open('test40su', mode='r') as f:
        line = f.readline()

        while line:
            lines = line.split( )
            hap = 0
            # hap = sum([float(i) for i in line.split()])
            # print("각 행의 숫자 합:", hap)
            for i in range(len(lines)):
                hap += float(lines[i])
            print(hap)
            line = f.readline()
except Exception as e:
    print('파일 처리 오류 : ', e)
