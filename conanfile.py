#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, tools
import os


class TLSFConan(ConanFile):
    name = "tlsf"
    version = "3.1"
    url = "https://github.com/bincrafters/conan-tlsf"
    description = "Two-Level Segregated Fit memory allocator implementation."

    # Indicates License type of the packaged library
    license = "BSD"

    # Packages the license for the conanfile.py
    exports = ["LICENSE.md"]

    # Remove following lines if the target lib does not use cmake.
    exports_sources = ["CMakeLists.txt"]
    generators = "cmake"

    # Options may need to change depending on the packaged library.
    settings = "os", "arch", "compiler", "build_type"
    options = {"shared": [True, False]}
    default_options = "shared=False"

    # Custom attributes for Bincrafters recipe conventions
    source_subfolder = "source_subfolder"
    build_subfolder = "build_subfolder"

    # Use version ranges for dependencies unless there's a reason not to

    def source(self):
        source_url = "https://github.com/mattconte/tlsf"
        tools.get("{0}/archive/master.zip".format(source_url, self.version))
        extracted_dir = self.name + "-master"

        #Rename to "source_subfolder" is a convention to simplify later steps
        os.rename(extracted_dir, self.source_subfolder)


    def build(self):
        cmake = CMake(self)
        cmake.configure(build_folder=self.build_subfolder)
        cmake.build()
        cmake.install()

    def package(self):
        # If the CMakeLists.txt has a proper install method, the steps below may be redundant
        # If so, you can replace all the steps below with the word "pass"
        pass


    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
