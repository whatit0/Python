from pack2.test30_ex2etc import ElecProduct

class ElecTv(ElecProduct):
    def volumeControl(self, volume):
        self.volume += volume
        print('Tv 소리 크기는 ' + str(self.volume))



class ElecRadio(ElecProduct):
    def showProduct(self):
        print('라디오 고유 메소드')

    def volumeControl(self, volume):
        vol = volume
        self.volume += vol
        print('Radio 소리 크기는 ', self.volume)

tv = ElecTv()
radio = ElecRadio()
tv.volumeControl(7)
tv.volumeControl(-3)
print()
radio.volumeControl(5)
radio.volumeControl(-5)

print('\n--------------------')
product = tv
product.volumeControl(10)
print()
product = radio
product.volumeControl(10)
