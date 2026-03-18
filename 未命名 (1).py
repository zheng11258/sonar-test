# knn函数
def my_knn(k,x,x_now,y):
    dist_all = np.array(dist_obtain(x,x_now))
    indices = np.argpartition(dist_all, k)[:k]
    print(f"数组中最小的 {k} 个数据的位置是: {indices}")
    k_label = y[indices]
    
    plt.scatter(x[y[:,0]==1,0],x[y[:,0]==1,1],color='g')
    plt.scatter(x[y[:,0]==0,0],x[y[:,0]==0,1],color='r')
    for i in indices:
        temp = np.vstack((x_now[0,:],x[i,:]))
        plt.plot(temp[:,0],temp[:,1],color='blue',linestyle='--')
    plt.scatter(x_now[0,0],x_now[0,1],color='k',marker='^')
    plt.show()
    
    k_label = y[indices]*2-1 
    
    jdg = np.sum(k_label)
    
    if jdg > 0:
        print('依据预测，x_now类型为绿色类型')
    elif jdg == 0:
        print('不能预测x_now的类型')
    else:
        print('依据预测，x_now类型为红色类型')