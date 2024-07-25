from copy_dic import copy_dic, generate_page_recursive

def main():
    copy_dic('static', 'public')
    generate_page_recursive('content', 'template.html', 'public')

if __name__ == "__main__":
    main()
