from copy_dic import copy_dic, generate_page

def main():
    copy_dic('static', 'public')
    generate_page('content/index.md', 'template.html', 'public/index.html')

if __name__ == "__main__":
    main()
