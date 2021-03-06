import os
import platform
import faster_os
# import faster_os_py

if platform.system() == 'Windows':
    from win.test_paths import paths, join_paths, valid_list_paths, rel_paths, norm_paths, list_paths, rel_paths, norm_paths, valid_list_paths
else:
    from unix.test_paths import paths, join_paths, list_paths, rel_paths, norm_paths, valid_list_paths

os_vs_fasteros_map = [
    (
        'split',
        os.path.split,
        faster_os.path.split,
    ),
    (
        'splitdrive',
        os.path.splitdrive,
        faster_os.path.splitdrive,
    ),
    (
        'normcase',
        os.path.normcase,
        faster_os.path.normcase,
    ),
    (
        'splitext',
        os.path.splitext,
        faster_os.path.splitext,
    ),
    (
        'join',
        os.path.join,
        faster_os.path.join,
        join_paths,
        True,
    ),
    (
        'relpath',
        os.path.relpath,
        faster_os.path.relpath,
        rel_paths,
        True,
    ),
    (
        'ismount',
        os.path.ismount,
        faster_os.path.ismount,
    ),
    (
        'normpath',
        os.path.normpath,
        faster_os.path.normpath,
        norm_paths,
        False,
    ),
    (
        'expanduser',
        os.path.expanduser,
        faster_os.path.expanduser,
    ),
    (
        'abspath',
        os.path.abspath,
        faster_os.path.abspath,
    ),
    (
        'isabs',
        os.path.isabs,
        faster_os.path.isabs,
    ),
    (
        'basename',
        os.path.basename,
        faster_os.path.basename,
    ),
    (
        'dirname',
        os.path.dirname,
        faster_os.path.dirname,
    ),
    (
        'commonpath',
        os.path.commonpath,
        faster_os.path.commonpath,
        valid_list_paths,
        False,
    ),
    (
        'commonprefix',
        os.path.commonprefix,
        faster_os.path.commonprefix,
        valid_list_paths,
        False,
    ),
]

# fasteros_vs_fasterospy_map = [
#     (
#         'split',
#         faster_os_py.path.split,
#         faster_os.path.split,
#     ),
#     (
#         'splitdrive',
#         faster_os_py.path.splitdrive,
#         faster_os.path.splitdrive,
#     ),
#     (
#         'normcase',
#         faster_os_py.path.normcase,
#         faster_os.path.normcase,
#     ),
#     (
#         'splitext',
#         faster_os_py.path.splitext,
#         faster_os.path.splitext,
#     ),
#     (
#         'join',
#         faster_os_py.path.join,
#         faster_os.path.join,
#         join_paths,
#         True,
#     ),
#     (
#         'relpath',
#         faster_os_py.path.relpath,
#         faster_os.path.relpath,
#         rel_paths,
#         True,
#     ),
#     (
#         'ismount',
#         faster_os_py.path.ismount,
#         faster_os.path.ismount,
#     ),
#     (
#         'normpath',
#         faster_os_py.path.normpath,
#         faster_os.path.normpath,
#         norm_paths,
#         False,
#     ),
#     (
#         'expanduser',
#         faster_os_py.path.expanduser,
#         faster_os.path.expanduser,
#     ),
#     (
#         'abspath',
#         faster_os_py.path.abspath,
#         faster_os.path.abspath,
#     ),
#     (
#         'isabs',
#         faster_os_py.path.isabs,
#         faster_os.path.isabs,
#     ),
#     (
#         'basename',
#         faster_os_py.path.basename,
#         faster_os.path.basename,
#     ),
#     (
#         'dirname',
#         faster_os_py.path.dirname,
#         faster_os.path.dirname,
#     ),
#     (
#         'commonpath',
#         faster_os_py.path.commonpath,
#         faster_os.path.commonpath,
#         valid_list_paths,
#         False,
#     ),
#     (
#         'commonprefix',
#         faster_os_py.path.commonprefix,
#         faster_os.path.commonprefix,
#         valid_list_paths,
#         False,
#     ),
#     (
#         'multi_split',
#         faster_os_py.path.multi_split,
#         faster_os.path.multi_split,
#         valid_list_paths,
#         False,
#     ),
# ]

faster_os_multi_os = [
    (
        'multi_commonpath',
        os.path.commonpath,
        faster_os.path.multi_commonpath,
        valid_list_paths,
        False,
    ),
    (
        'multi_commonprefix',
        os.path.commonprefix,
        faster_os.path.multi_commonprefix,
        valid_list_paths,
        False,
    ),
    (
        'multi_abspath',
        os.path.abspath,
        faster_os.path.multi_abspath,
        paths,
    ),
    (
        'multi_ismount',
        os.path.ismount,
        faster_os.path.multi_ismount,
        paths,
    ),
    (
        'multi_expanduser',
        os.path.expanduser,
        faster_os.path.multi_expanduser,
        paths,
    ),
    (
        'multi_relpath',
        os.path.relpath,
        faster_os.path.multi_relpath,
        rel_paths,
        True,
    ),
    (
        'multi_split',
        os.path.split,
        faster_os.path.multi_split,
        paths,
    ),
    (
        'multi_splitdrive',
        os.path.splitdrive,
        faster_os.path.multi_splitdrive,
        paths,
    ),
    (
        'multi_normcase',
        os.path.normcase,
        faster_os.path.multi_normcase,
        paths,
    ),
    (
        'multi_normpath',
        os.path.normpath,
        faster_os.path.multi_normpath,
        norm_paths,
    ),
    (
        'multi_basename',
        os.path.basename,
        faster_os.path.multi_basename,
        paths,
    ),
    (
        'multi_dirname',
        os.path.dirname,
        faster_os.path.multi_dirname,
        paths,
    ),
    (
        'multi_isabs',
        os.path.isabs,
        faster_os.path.multi_isabs,
        paths,
    ),
    (
        'multi_splitext',
        os.path.splitext,
        faster_os.path.multi_splitext,
        paths,
    ),
    (
        'multi_join',
        os.path.join,
        faster_os.path.multi_join,
        join_paths,
        True,
    ),
]

faster_os_multi_faster_os = [
    (
        'multi_commonpath',
        faster_os.path.commonpath,
        faster_os.path.multi_commonpath,
        valid_list_paths,
        False,
    ),
    (
        'multi_commonprefix',
        faster_os.path.commonprefix,
        faster_os.path.multi_commonprefix,
        valid_list_paths,
        False,
    ),
    (
        'multi_abspath',
        faster_os.path.abspath,
        faster_os.path.multi_abspath,
        paths,
    ),
    (
        'multi_ismount',
        faster_os.path.ismount,
        faster_os.path.multi_ismount,
        paths,
    ),
    (
        'multi_expanduser',
        faster_os.path.expanduser,
        faster_os.path.multi_expanduser,
        paths,
    ),
    (
        'multi_relpath',
        faster_os.path.relpath,
        faster_os.path.multi_relpath,
        rel_paths,
        True,
    ),
    (
        'multi_split',
        faster_os.path.split,
        faster_os.path.multi_split,
        paths,
    ),
    (
        'multi_normpath',
        faster_os.path.normpath,
        faster_os.path.multi_normpath,
        norm_paths,
    ),
    (
        'multi_splitdrive',
        faster_os.path.splitdrive,
        faster_os.path.multi_splitdrive,
        paths,
    ),
    (
        'multi_normcase',
        faster_os.path.normcase,
        faster_os.path.multi_normcase,
        paths,
    ),
    (
        'multi_basename',
        faster_os.path.basename,
        faster_os.path.multi_basename,
        paths,
    ),
    (
        'multi_dirname',
        faster_os.path.dirname,
        faster_os.path.multi_dirname,
        paths,
    ),
    (
        'multi_isabs',
        faster_os.path.isabs,
        faster_os.path.multi_isabs,
        paths,
    ),
    (
        'multi_splitext',
        faster_os.path.splitext,
        faster_os.path.multi_splitext,
        paths,
    ),
    (
        'multi_join',
        faster_os.path.join,
        faster_os.path.multi_join,
        join_paths,
        True,
    ),
]
