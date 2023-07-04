

def decorator_imprimir(funcao):
      def wrapper(capital, juros, tempo):
             resultado = funcao ( capital, juros, tempo)
             print (f"parametros: Capital={capital}, Juros={juros}, Tempo={tempo}")
             print (f"Resultado: {resultado}")
             return resultado

    
      return wrapper    


        

@decorator_imprimir
def juros_simples (capital ,juros ,tempo):
       resl = (capital * (juros/ 100) * tempo)
       return resl



juros = juros_simples(100,2.1,10)
print( f"Juros: {juros}")
