- 👋 Hi, I’m @bashmitzy
- 👀 I’m interested in machine learning, simulation, education
- 🌱 I’m currently learning education techniques
- 💞️ I’m looking to collaborate on simulation, computer vision and machine learning projects
- 📫 How to reach me  bash_mitzy@yahoo.com

<!---
bashmitzy/bashmitzy is a ✨ special ✨ repository because its `README.md` (this file) appears on your GitHub profile.
You can click the Preview link to take a look at your changes.
--->
El pendulo simple es un problema clásico de fisica, teoria de control, matemáticas, etc.

![image](https://user-images.githubusercontent.com/13348364/152711656-4b1d2643-8e7b-48f0-88e8-cf38622df2cf.png)

El eje de referencia es el eje vertical y coincide con la posición θ = 0, a partir de allí se mide el desplazamiento angular θ, ya sea en un sentido o en otro. Se puede asignar el signo + al desplazamiento hacia la derecha en la figura.

Por otro lado, la velocidad tangencial varía por el movimiento contra el efecto de la gravedad:

-mg sen(θ)+  (m* d^2 s)/(dt^2 )=0   			                        Ec 1.4.3a

La ecuación 1.4.3a marca la fuerza negativa debida a la gravedad, contra la fuerza positiva debida al movimiento de la partícula en el péndulo.
La ecuación 1.4.3a no considera la fricción del péndulo por rozamiento de la parte móvil, ni por el rozamiento del aire.

La derivada del arco es la pendiente de una recta tangente, o la velocidad tangencial.
La doble derivada del arco es la aceleración tangencial. La masa por la aceleración tangencial es la fuerza debida al movimiento inercial, que va disminuyendo por el efecto de la gravedad

La longitud de un arco de circunferencia de radio r y ángulo θ (medido en radianes), con el centro en el origen, es igual a θ*r.   L es la longitud de la cuerda, o el radio r
s= L* θ.    Longitud de arco= Largo del péndulo * ángulo. 

Antes de despejar la variable, asumimos que la dimensión del arco s varía de acuerdo a la longitud del colgante que sostiene a la masa del péndulo, multiplicada por el ángulo.
s= L* θ

s(t)= L* θ(t), 

derivamos s(t)

ds/dt=L*  dθ/dt

Derivamos de nuevo s(t)

(d^2 s)/(dt^2 )=L*  (d^2 θ)/(dt^2 )                                              Ec 1.4.3b

Sustituyendo Ec 1.4.3b en la ecuación 1.4.3a

-m*g*sen(θ)+m* L*  (d^2 θ)/(dt^2 )=0                                             Ec 1.4.3c

Eliminanos m por ser factor común contra cero,

-g*sen(θ)+ L*  (d^2 θ)/(dt^2 )=0                                                 Ec 1.4.3d

Haciendo θ=sen(θ), válido para ángulos pequeños,

-g*θ+ L*  (d^2 θ)/(dt^2 )=0                                                      Ec 1.4.3e

Despejando para hacer más clara la ecuación diferencial que debemos resolver:

  (d^2 θ)/(dt^2 )=(-g)/L* θ                       					                     Ec 1.4.3f


Se busca una función que al derivarla dos veces se obtenga la misma función, multiplicada por el factor –g/L, que es una constante.
Las funciones obvias son seno, coseno, o exponenciales. La mejor selección es la función seno o coseno. 

No puede ser la exponencial por lo siguiente:
Con exponencial positiva:
F(x)=e^x     f ’(x)= e^x    f ‘ ‘(x)= e^x

Con exponencial negativa:
F(x)=e^ -x     f ’(x)= -e^ -x    f ‘ ‘(x)=  e^-x

En la exponencial no se cumple el cambio de signo al hacer la segunda derivada.

Si se considera la función coseno
	
θ(t)=A*cos⁡(ωt+φ)                        				         Ec 1.4.3g

La Ec 1.4.3g corresponde al movimiento armónico simple. En este, el movimiento es cíclico, repitiendo la misma trayectoria y coincidiendo el máximo del ángulo (positivo o negativo) con el valor cero en la velocidad.
ω es la frecuencia angular, φ es el ángulo de defase.

La primera derivada de la Ec 1.4.3g es 

θ^' (t)=-A*ω*sen⁡(ωt+φ)           Velocidad Angular                      

La segunda derivada de la Ec 1.4.3g es 

〖θ^''〗^ (t)=-A*ω*ω*cos⁡(ωt+φ)= -A*ω^2*cos⁡(ωt+φ)      Aceleración angular                        

Sustituyendo en la Ec 1.4.3f:

-A*ω^2*cos⁡(ωt+φ)=  (-g)/L*A*cos⁡(ωt+φ)

Cancelamos el coseno y la magnitud A, por ser factor común contra el  cero,

-ω^2=  (-g)/L  

ω= √(g/L)  

La frecuencia de oscilación del péndulo, ω, depende de la gravedad y del largo del colgante.

