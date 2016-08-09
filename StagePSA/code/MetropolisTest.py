import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

def main():
    """An implementation of Metropolis-Hastings algorithm.

    Parameters:
        F (lambda function): function to minimize (default=0.25*x^4 - 10*x^2 + 10*x)
        start (float) : domain to minimize (default=-6).
        end (float) : domain to minimize (default=6)
        mode ('GlobalExplore' or 'LocalExplore'): allow or not the system to jump from one state to another faraway. (default='LocalExplore').
        localRange (float): furthest state that the system can jump to, in case mode is set to 'LocalExplore' (default=1).
        N (int) : number of iteration (default=1000).

    Note:
        To set up quadratic time, use ``beta = beta + (step*(2*i+1))/N`` in the end of ``for`` loop. If you want to use linear time,
        set ``beta = beta + step``.


    Reference:
        `Metropolis-Hastings algorithm <https://en.wikipedia.org/wiki/Metropolis-Hastings_algorithm>`_
    """
    F = lambda x : 1./4*x**4 - 10*x**2 + 10*x
    #F = lambda x : np.sin(x)
    start = -6
    end = 6
    x = np.linspace(start,end,500)

    #a = np.random.random()*(end - start) + start
    a = 5
    trueValue = [F(a)]
    beta = 0
    #step = 0.0001
    N = 1000
    step = 1./(N)



    fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(12,5))
    axes[0].plot(x, map(F,x))
    axes[0].set_xlim(start, end)
    axes[1].set_xlim(-1,N+1)
    axes[2].set_xlim(-1,N+1)
    axes[2].set_ylim(0,5)

    colors = cm.inferno(np.linspace(0,1,N))

    #mode = 'GlobalExplore'
    mode = 'LocalExplore'
    localRange = 1
    axes[1].scatter(0, F(a), s=5, c='red')
    axes[2].scatter(0, beta, s=5, c='red')
    for i in range(1,N):
        Fa = F(a)
        axes[0].scatter(a, Fa, s=5, c=colors[i])
        if mode == 'GlobalExplore':
            b = np.random.random()*(end - start) + start
        elif mode == 'LocalExplore':
            b = a + (np.random.random()*2 - 1)*localRange
            if b < start:
                b = start
            if b > end:
                b = end
        Fb = F(b)
        if Fb < Fa:
            a = b
            print str(i) + " : Accept, lower energy: x = " + str(a) + ", y = " + str(Fa)
        else:
             prob = np.random.random()
             if prob < np.exp(-beta * (Fb-Fa)):
                 a = b
                 print str(i) + " : Accept, higher energy: x = " + str(a) + ", y = " + str(Fa)
             else:
                 print str(i) + " : Reject"
        trueValue = trueValue + [Fa]
        axes[1].scatter(i, Fa, s=5, c=colors[i])
        beta = beta + (step*(2*i+1))/N
        #beta = beta + step
        axes[2].scatter(i+1, beta, s=5, c='red')
        #plt.pause(0.00001)

    axes[0].scatter(a, F(a), s=50, c='red')
    axes[1].plot(np.array(range(len(trueValue))), trueValue)
    plt.pause(1)

if __name__ == "__main__":
    main()
