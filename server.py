import routes

__author__ = 'mjholler'

def main():
    from werkzeug.serving import run_simple
    run_simple('localhost', 8080, routes.app, use_reloader=True)

if __name__ == '__main__':
    main()