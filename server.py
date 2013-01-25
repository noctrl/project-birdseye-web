from werkzeug.serving import run_simple
import routes

__author__ = 'mjholler'


def main():
    try:
        run_simple('localhost', 8080, routes.app, use_reloader=True)
    except Exception as e:
        main()

if __name__ == '__main__':
    main()