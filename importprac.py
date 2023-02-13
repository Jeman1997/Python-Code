class Category:
    def __init__(self,cat):
        self.categ  = cat
        self.ledger = []
    
    def deposit(self,amount,description=''):
        self.ledger.append({'amount':amount,'description':description})
        
    def withdraw(self,w_amount,w_description=''):
        amnt=self.get_balance()
        if amnt<w_amount:
            return False
        else:
            self.ledger.append({'amount':(0-w_amount),'description':w_description})
            return True
        
    def transfer(self,t_amount,bud_cat):
        amnt=self.get_balance()
        if amnt<t_amount:
            return False
        else:
            self.withdraw(t_amount,'Transfer to '+bud_cat.categ)
            bud_cat.deposit(t_amount,'Transfer from '+self.categ)
            return True
        
    def get_balance(self):
        return sum([x['amount'] for x in self.ledger])
    
    def check_funds(self,amnt):
        return not amt>sum([x['amount'] for x in self.ledger])
    def __str__(self):
        if len(self.categ)%2==0:
            fl= ('*'*int(15-(len(self.categ)/2)))+self.categ+('*'*(15-int(len(self.categ)/2)))
        else:
            fl=("*"*int(30-len(self.categ))+self.categ)
        nxtl = '\n'
        for x in self.ledger:
            if len(x['description'])>23:
                desc=x['description'][:23]
            else:
                desc=x['description']
            ttamt = '{:.2f}'.format(x['amount'])
            nxtl+=desc+(' '*(30-len(ttamt)-len(desc)))+ttamt+'\n'
        tt='Total: '+str(self.get_balance())
        return fl+nxtl+tt
food=Category('Food')
entertainment=Category('Entertainment')
business=Category('Business')
food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)

def create_spend_chart(categories):
    lwith=[]
    for i in categories:
        w_amt=0
        for x in i.ledger:
            w_s_amt=x['amount']
            if w_s_amt<0:
                w_amt+=w_s_amt
        lwith.append(w_amt)
    slwith=sum(lwith)
    lwithper=[]
    lwithfl=[]
    for y in lwith:
        lwithfl.append((100/sum(lwith))*y)
    for y in lwith:
        #eper=int((((100/sum(lwith))*y)-(((100/sum(lwith))*y)%10)))
        #if eper==0:
        #  lwithper.append(10)
        #else:
        lwithper.append(int((((100/sum(lwith))*y)-(((100/sum(lwith))*y)%10))))
    head='Percentage spent by category\n'
    max_lbl_len=3
    ls=''
    bas=len(categories)*3
    for l in range(100,-10,-10):
        noofos=''
        for x in lwithper:
            if l<=x:
                noofos+=('o  ')
            else:
                noofos+=('   ')
        ls+=(' '*abs(max_lbl_len-len(str(l))))+str(l)+'|'+' '+noofos+'\n'
    ds='    '+'-'+('-'*bas)
    catlst=[]
    for x in categories:
        catlst.append([i for i in x.categ.capitalize()])
    lls=''
    ml = max([len(u) for u in catlst])
    for x in range(ml):
        el=''
        for r in catlst:
            if x<len(r):
                el+=r[x]+'  '
            else:
                el+='   '
        lls+='\n     '+el
  
    return (head+ls+ds+lls)       
    
firmy=(create_spend_chart([business,food,entertainment]))
fir=('Percentage spent by category\n100|          \n 90|          \n 80|          \n 70|    o     \n 60|    o     \n 50|    o     \n 40|    o     \n 30|    o     \n 20|    o  o  \n 10|    o  o  \n  0| o  o  o  \n    ----------\n     B  F  E  \n     u  o  n  \n     s  o  t  \n     i  d  e  \n     n     r  \n     e     t  \n     s     a  \n     s     i  \n           n  \n           m  \n           e  \n           n  \n           t  ')
print(firmy)
print(fir)
print(len(firmy)
      )
print(len(fir))
print(firmy==fir)