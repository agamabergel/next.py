def a(ch, rang):
    return "{}$".format(f'{ch}, '.join([str(i) for i in rang]))



if __name__ == "__main__":
    print(a("$", range(23)))

    
