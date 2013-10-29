AR = '/usr/bin/ar'
ARFLAGS = 'rcs'
BINDIR = '/usr/local/bin'
CC_VERSION = ('4', '7', '3')
CFLAGS = ['-I/home/gian/mod/src_plugins/mda-lv2', '-DNDEBUG', '-fshow-column']
CHECKED_LV2 = 2
COMPILER_CXX = 'g++'
CPPPATH_ST = '-I%s'
CXX = ['/usr/bin/g++']
CXXFLAGS = ['-I/home/gian/mod/src_plugins/mda-lv2', '-DNDEBUG', '-fshow-column']
CXXFLAGS_MACBUNDLE = ['-fPIC']
CXXFLAGS_cxxshlib = ['-fPIC']
CXXLNK_SRC_F = []
CXXLNK_TGT_F = ['-o']
CXX_NAME = 'gcc'
CXX_SRC_F = []
CXX_TGT_F = ['-c', '-o']
DATADIR = '/usr/local/share'
DEBUG = False
DEFINES = ['HAVE_LV2=1']
DEFINES_ST = '-D%s'
DEST_BINFMT = 'elf'
DEST_CPU = 'x86_64'
DEST_OS = 'linux'
DOCDIR = '/usr/local/share/doc'
DOCS = False
INCLUDEDIR = '/usr/local/include'
LIBDIR = '/usr/local/lib'
LIBPATH_ST = '-L%s'
LIB_ST = '-l%s'
LINKFLAGS_MACBUNDLE = ['-bundle', '-undefined', 'dynamic_lookup']
LINKFLAGS_cxxshlib = ['-shared']
LINKFLAGS_cxxstlib = ['-Wl,-Bstatic']
LINK_CXX = ['/usr/bin/g++']
LV2DIR = '/usr/local/lib/lv2'
MANDIR = '/usr/local/share/man'
PARDEBUG = False
PKGCONFIG = '/usr/bin/pkg-config'
PKG_lv2 = 'lv2'
PREFIX = '/usr/local'
RPATH_ST = '-Wl,-rpath,%s'
SHLIB_MARKER = '-Wl,-Bdynamic'
SONAME_ST = '-Wl,-h,%s'
STLIBPATH_ST = '-L%s'
STLIB_MARKER = '-Wl,-Bstatic'
STLIB_ST = '-l%s'
SYSCONFDIR = '/usr/local/etc'
VERSION_lv2 = '1.0.0'
cxxprogram_PATTERN = '%s'
cxxshlib_PATTERN = 'lib%s.so'
cxxstlib_PATTERN = 'lib%s.a'
define_key = ['HAVE_LV2']
macbundle_PATTERN = '%s.bundle'