import os


class FileUploadMaster:
    dir_name = 'static/files'
    path = dir_name

    @classmethod
    def check_upload_dir(cls):
        status = os.path.exists(cls.dir_name)
        if not status:
            try:
                os.mkdir(cls.dir_name)
            except Exception as e:
                print(f'Error! {e}')
                return False
        return os.path.exists(cls.dir_name)

    @classmethod
    def make_dir(cls, name):
        check_status = cls.check_upload_dir()
        if not check_status:
            return False
        correction_dir_path = os.path.join(cls.dir_name, name)
        status = os.path.exists(correction_dir_path)
        if not status:
            try:
                os.mkdir(correction_dir_path)
            except Exception as e:
                print(f'Error! {e}')
                return False
        return correction_dir_path

    @classmethod
    def handle_uploaded_file(cls, file, name):
        upload_path = cls.make_dir(name)
        if upload_path:
            path = os.path.join(upload_path, str(file))
            with open(path, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            return path
        return None
