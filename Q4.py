from plotting import plot
n1=complex(input("Enter 1st complex number:"))
n2=complex(input("Enter 2nd complex number:"))
n3=complex(input("Enter 3rd complex number:"))
n4=complex(input("Enter 4th complex number:"))
n5=complex(input("Enter 5th complex number:"))

S={n1, n2, n3, n4, n5}

#Scaling
scal=int(input("Enter a scalar value:"))
S3={(scal)*z for z in S}
plot (S3,100)
