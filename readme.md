```bash
cmake -DDEAL_II_WITH_PETSC=OFF -DDEAL_II_PETSC_WITH_COMPLEX=OFF -DDEAL_II_WITH_P4EST=OFF -DDEAL_II_WITH_TRILINOS=OFF ..
```

<title>The deal.II Readme</title>

<meta http-equiv="Content-Type" content="text/html;charset=utf-8">

<link href="screen.css" rel="StyleSheet">

<meta name="copyright" content="Copyright (C) 1998 - 2020 by the deal.II Authors">

<meta name="keywords" content="deal.II">

Installation instructions and further information on 

<acronym>deal.II</acronym>
=================================================================================

<div class="toc">
    1.  System requirements

        1.  Supported platforms
        2.  Additional software requirements
    2.  Installation

        1.  Unpacking
        2.  Configuring and building the library
        3.  Configuring and building the documentation
        4.  Configuration options

            1.  Selecting optional compilation features
            2.  Selecting optional library features
            3.  Optional interfaces to
                		other software packages
            4.  More information on configuring
                		and building the library
    3.  License
</div>    

System requirements
-------------------



### Supported platforms



<acronym>deal.II</acronym> is mostly developed on Linux using the
[GCC](http://gcc.gnu.org) compiler. However, it is not platform specific and we strive to keep the source code compliant with the [C++ 2011
Standard](https://www.iso.org/standard/50372.html) (see also [here](http://www.open-std.org/jtc1/sc22/wg21/docs/papers/2012/n3337.pdf) for a copy of the C++11 standard).

<acronym>deal.II</acronym> supports at least the following platforms:

* GNU/Linux: GCC version 4.9 or later; Clang version 4.0 or later; ICC versions 15 or later
* Mac OS X: GCC version 4.9 or later; Clang version 4.0 or later. Please see the [deal.II Wiki](https://github.com/dealii/dealii/wiki/MacOSX) for installation instructions.
* Windows: experimental support for Visual Studio 2017. Please have a look at the
                [      FAQ](https://github.com/dealii/dealii/wiki/Frequently-Asked-Questions#can-i-use-dealii-on-a-windows-platform) and at the [deal.II Wiki](https://github.com/dealii/dealii/wiki/Windows) for more information and alternative solutions.

Most other combinations of POSIX-style operating systems and C++ Standard compliant compilers should also work. _If they don't,
please report it as a bug._


### Additional software requirements

In order to compile and use 
<acronym>deal.II</acronym> you need to have the following programs installed:

* [CMake](http://www.cmake.org/) version 2.8.12 or later

* [GNU make](http://www.gnu.org/software/make/), version 3.78 or later (or any other generator supported by CMake)

*             For generating the documentation:
                [Perl 5.x](http://www.perl.org/),
                [doxygen](http://www.doxygen.org/) and `dot`, which is part of the
                [GraphViz](http://www.graphviz.org) package

*             For debugging programs, we have found that the
                [GNU
    	    debugger GDB](http://www.gnu.org/software/gdb/) is an invaluable tool. GDB is a text-based tool not always easy to use; [kdbg](http://www.kdbg.org/), is one of many graphical user interfaces for it. Most integrated development environments
                like [kdevelop](http://www.kdevelop.org/) or [Eclipse](http://eclipse.org/) have built in debuggers as well. 

    <acronym>deal.II</acronym> has some support for pretty printing its own classes
                through GDB; see [the GDB configuration guide](users/gdb.html) for setup information.


* The library generates output in formats readable by
    [GNUPLOT](http://www.gnuplot.info/),
    [GMV
    (general mesh viewer)](http://www.generalmeshviewer.com/),
    [Tecplot](http://www.tecplot.com/) (ASCII and binary),
    [Visualization Toolkit (Vtk)](http://www.vtk.org/),
    [AVS Explorer](http://www.avs.com),
    [Open DX](http://www.opendx.org),
    [Povray](http://www.povray.org), and directly to Encapsulated Postscript.

    `gnuplot` and a postscript viewer (for `eps`) should be available almost everywhere. In the last few years, most new visualization programs have moved to support
    `vtk`/`vtu` format. There are a number of excellent programs that can read `vtk` and
    `vtu`, such as
    [VisIt](http://www.llnl.gov/visit/),
    [ParaView](http://www.paraview.org/), as well as others. Povray is freely available for almost all platforms. AVS is a commercial program available for most Unix flavors. Tecplot is a commercial program available
    for Windows and most Unix platforms.

    In case you didn't find your favorite graphics format above, adding a new writer to 
    <acronym>deal.II</acronym> is not too difficult, as only a simple intermediate format needs to be converted into output (without references to cells, nodes,
    types of finite elements, and the like).



Installation
------------


### Unpacking

The whole library usually comes as a `tar.gz` file, which is a file archive compressed with gzip. After downloading it, unpack it using either

<pre>
  gunzip deal.II-X.Y.Z.tar.gz
  tar xf deal.II-X.Y.Z.tar

</pre>

or, if you have GNU tar with

<pre>
  tar -xvf deal.II-X.Y.Z.tar.gz

</pre>

**Note:** You will want to hang on to the source files of 
<acronym>deal.II</acronym> after installation as it makes developing much simpler. Consequently, you should do the steps above in a permanent directory, not on `/tmp` as one often
does when installing software.



### Configuring and building the library

<acronym>deal.II</acronym> uses the
[CMake](http://www.cmake.org/) integrated configuration and build system. Unpacking will create a subdirectory 
<tt>deal.II/</tt> in the current directory. Then do the following steps to configure the build process (make sure the installation directory is not the same as the location where you unpacked 
<tt>deal.II/</tt>):

<pre>
  mkdir build
  cd build
  cmake -DCMAKE_INSTALL_PREFIX=/path/to/install/dir ../deal.II

</pre>
    We recommend compiling deal.II in parallel if your machine has
    more than one processor core. This can be done by providing
    the `--jobs=N` flag to `make` with a
    numerical argument `N`. (The
    argument `--jobs=N` is often abbreviated
    as `-jN`.) Here we compile with four `make`
    jobs:


<pre>
  make --jobs=4 install
  make test

</pre>
    One should usually use one job for each processor core on the
    machine.



These steps compile, link, install the deal.II library, and run a few consistency checks. The whole process should take between a few minutes and an hour, depending on your machine.

**Notes:**

*  The part "`/path/to/install/dir`" in the
                command above needs to be replaced by the path to the directory which deal.II should be installed into. This can be a directory in your home directory (e.g., `~/bin/deal.II`) or a directory such as `/usr/local` if you have root privileges.
                Another option is to use something like ```pwd`/../installed/`` (note the backticks).

* `make test` automatically runs in parallel and no `-jN` flag should be supplied to it.

*  If you do not intend to modify the 

    <acronym>deal.II</acronym> sources and recompile things, then you can remove the `build/` directory after the last step.


*  In principle, after installing 

    <acronym>deal.II</acronym>, you can remove the source directory as well (i.e., the directory into which `tar` unpacked the file you downloaded) since projects using deal.II should only need files that
                have been installed. However, you will find it convenient to keep the source files around anyway, for one reason: When debugging you often end up with assertions for which you'd like to see the place in the library's source files that triggered
                it.


*  The 

    <acronym>deal.II</acronym>`CMake` system can accept a significant number of configuration parameters. See the discussion below.


*  If you are changing part of the 

    <acronym>deal.II</acronym> code itself, you can re-compile the library using only the last two commands above in the previously created build directory. It is also possible to change the configuration used in this
                directory by calling `cmake` a second time, possibly with different arguments. However, this sometimes leads to surprising results and you may not get exactly what you were hoping for. For more information, see [here](users/cmake_dealii.html).


*           Compilers require a lot of memory. If your machine has many
              cores but not so much memory, then using `-jN`
              with a large `N` might lead to situations where
              not enough memory is available for all compilers, and this
              typically manifests as an "internal compiler error" or a
              segmentation fault. If that happens, just
              reduce `N` and type the `make install`
              command again.


The commands above build and install the 
<acronym>deal.II</acronym> libraries in two variants:

* _Debug mode_: This version of the library is compiled with compiler flags so that the library contains information that can be used by debuggers.

    In addition, this library contains a great number of safety checks on most arguments of all functions you could possibly call. These assertions have proven to be an invaluable means to finding programming bugs since they will almost always abort your
    program if something goes wrong. In our experience, more than ninety per cent of all errors are invalid parameters (such as vectors having the wrong size, etc.) and they are usually found almost instantaneously, displaying the file name
    and line number of where the problem occurred.

    With GCC Debug mode, by default, uses the `-Og` flag. It promises most of the debugging experience of `-O0` but at a better performance. This is a reasonable choice for unit tests and enables numerous asserts within
    the library. Sometimes, however, one needs Debug mode to use
    `-O0`, where all compiler optimizations are avoided and code and variables are exactly as indicated in the C++ program (e.g. with `-Og` GCC 6.2.0 optimizes out local variables). This can be achieved by configuring
    <acronym>deal.II</acronym> with
    `-DDEAL_II_HAVE_FLAG_Og=false`.

* _Optimized mode_: You will want to link with this version of the library once you know that your program is working as expected. It does not contain the safety checks any more and is compiled with aggressive compiler optimizations. The resulting
                executables are smaller and will run between 2 and 10 times faster than the debug executables.


At this point, you have generated everything necessary to write programs based on 
<acronym>deal.II</acronym>. If you are new to
<acronym>deal.II</acronym>, you may want to continue with the
[tutorial](doxygen/deal.II/Tutorial.html).



### Configuring and building the documentation

All the documentation about the version that you downloaded and that can be found at the [      http://www.dealii.org/](http://www.dealii.org/) domain can also be generated locally. To do so, invoke `cmake` in the build instructions above as follows:

<pre>
      cmake -DDEAL_II_COMPONENT_DOCUMENTATION=ON -DCMAKE_INSTALL_PREFIX=/path/install/dir ../deal.II
      make documentation
      make install

</pre>

As usual, you can pass `-jN` to `make`
in order to use more than one processor.
For this to succeed, you will need [Perl 5.x](http://www.perl.org/),
[doxygen](http://www.doxygen.org/) and `dot` (which is part of the [GraphViz](http://www.graphviz.org) package) to be installed.

The documentation contains links to pictures (e.g., for the tutorial programs) that are by default stored online at the dealii.org domain. If you want to use the documentation completely offline, you can run the `contrib/utilities/makeofflinedoc.sh`        script in an installed documentation directory to download all images.

Finally, the default for locally installed documentation is to render formulas as images. You can force formulas to be displayed via the MathJax system by adding `-DDEAL_II_DOXYGEN_USE_MATHJAX=ON` to the CMake call above. These formulas
are then rendered natively by the browser. With `-DDEAL_II_DOXYGEN_USE_ONLINE_MATHJAX=OFF` CMake will try to find a local installation of MathJax scripts, otherwise the online version of the scripts will be used in the documentation.

**Note:** Generating this documentation can take a _really long
time_ — running doxygen through our hundreds of thousands of lines of code can take 15-20 minutes even on a fast machine during which you will not get any output from `make`.



### Configuration options

<acronym>deal.II</acronym> has a large number of optional interfaces to other libraries. **By default, `cmake` will automatically
enable support  for all external libraries it can find in default
paths.** However, this behavior can be changed using command line switches to the initial call to `cmake`. A detailed description can be found here: [Detailed build system description](users/cmake_dealii.html).

In the following, let us summarize the most common configuration options.


#### Selecting optional compilation features


* _Unity build_: deal.II may be compiled with a unity build; that is, one may configure the build process so that the library is compiled as a few large files instead of many small ones. The unity build feature may be enabled by passing
                    the `-DDEAL_II_UNITY_BUILD=ON` argument to `cmake`. This feature is disabled by default.




#### Selecting optional library features




*             

    _Threading_: By default, deal.II supports parallelism between multiple cores on the same machine using threads and a task-based model built on the
    [Threading Building Blocks](http://threadingbuildingblocks.org/). You can switch threading off by passing the `-DDEAL_II_WITH_THREADS=OFF` argument to `cmake`.

* _MPI_: To enable parallel computations beyond a single node using the [Message
    Passing Interface (MPI)](http://mpi-forum.org/), pass the
    `-DDEAL_II_WITH_MPI=ON` argument to `cmake`. If `cmake` found MPI but you specifically do not want to use it, then pass `-DDEAL_II_WITH_MPI=OFF`.
    The minimal supported version is MPI-2.0.

* _64bit indices_: By default, deal.II uses
    unsigned int (32bit) indices for degrees of freedom,
    using the `types::global_dof_index` type.
    (The same is true for a few other index types such as the
    global number of cells.) This limits the number of
    cells or unknowns to approximately four billions. If
    larger problem must be solved, pass the
    `-DDEAL_II_WITH_64BIT_INDICES=ON` argument to
    `cmake`. To use this option with
    PETSc, PETSc must be compiled
    with the option `--with-64-bit-indices`.    

#### Optional interfaces to other software packages



When configuring interfacing to external libraries, the
`cmake` script by default tries to find all of these libraries in a number of standard locations on your file system. For _optional_ interfaces, it gives up if the library is not found and 
<acronym>deal.II</acronym> will be built
without support for them. However, there is one interface that we _need_ to have: [BOOST 1.59](http://www.boost.org/) or newer. If it is not found externally `cmake` will resort to the bundled boost version
that is part of the 
<acronym>deal.II</acronym> tar file.

The following paragraphs describe how the interfaces to the various packages, 
<acronym>deal.II</acronym> interacts with, can be configured.

**Notes:**

* **The majority of libraries mentioned below should be readily
              packaged by most Linux distributions. Usually you need to
              install a _development_ version of a library package,
              e.g. ending in `-dev` or `-devel`.
              After that `cmake` will automatically find the
              library and use it.**
*             Configuring the interface to a self compiled package, say `foo` can usually be done by specifying
                `-DFOO_DIR=/path/to/foo`. Alternatively, you can set `FOO_DIR` as an environment variable in your
                `.bashrc` or `.cshrc` file so that you do not have to enter this argument again the next time you invoke `cmake` in a fresh build directory. Any value passed on the command line wins over a value that may be
                found in an environment variable.

*             To explicitly enable or disable support for a library `foo` use the argument
                `-DDEAL_II_WITH_FOO=ON` resp.
                `-DDEAL_II_WITH_FOO=OFF` for `cmake`.


<dl>
    <dt>            [ADOL-C](https://projects.coin-or.org/ADOL-C)</dt>
    <dd>
        [ADOL-C](https://projects.coin-or.org/ADOL-C) is a package that facilitates the evaluation of first and higher derivatives of vector functions. In particular, it can be used for automatic differentiation. For using
        [ADOL-C](https://projects.coin-or.org/ADOL-C/) with deal.II, version 2.6.4 or newer is required. To use a self compiled version, pass
        `-DADOLC_DIR=/path/to/adolc` to the deal.II CMake call.

    </dd>
    <dt>	[ARPACK](http://www.caam.rice.edu/software/ARPACK/)</dt>
    <dd>
        [ARPACK](http://www.caam.rice.edu/software/ARPACK/) is a library for computing large scale eigenvalue problems.
        [ARPACK](http://www.caam.rice.edu/software/ARPACK/) should be readily packaged by most Linux distributions. To use a self compiled version, pass
        `-DARPACK_DIR=/path/to/arpack` to the deal.II CMake call. For a detailed description on how to compile ARPACK and linking with deal.II, see
        [this page](external-libs/arpack.html).

    </dd>
    <dt>             [Assimp](http://www.assimp.org/)</dt>
    <dd>
        [](http://www.assimp.org/) is a portable Open Source library to import various well-known 3D model formats in a uniform manner. A subset of these formats can be read from within deal.II to generate two-dimensional
        meshes, possibly embedded in a three-dimensional space.
        [Assimp](http://www.assimp.org/) should be readily packaged by most Linux distributions. To use a self compiled version, pass
        `-DASSIMP_DIR=/path/to/assimp` to the deal.II CMake call.

    </dd>
    <dt>	[BLAS](http://www.netlib.org/blas/),
    	[LAPACK](http://www.netlib.org/lapack/)</dt>
    <dd>
        [BLAS](http://www.netlib.org/blas/) (the _Basic Linear Algebra Subroutines_) and
        [LAPACK](http://www.netlib.org/lapack/) (
        _Linear Algebra Package_) are two packages that support low-level linear algebra operations on vectors and dense matrices. Both libraries should be packaged by almost all Linux distributions and found automatically whenever available.
        (You might have to install development versions of the libraries for 
        <acronym>deal.II</acronym> being able to use them). For details on how to set up 
        <acronym>deal.II</acronym> with a non standard BLAS/LAPACK implementation, see the
        [advanced
        setup](users/cmake_dealii.html#advanced) section in the CMake ReadME.

    </dd>
    <dt>[CUDA](https://developer.nvidia.com/cuda-zone)</dt>
    <dd>
        [CUDA](https://developer.nvidia.com/cuda-zone) is a parallel computing platform and API model created by Nvidia. It allows software developers and software engineers to use CUDA-enabled GPU for general purpose processing. Details
        about compatibility and configuration can be found [here](external-libs/cuda.html).

    </dd>
    <dt>                [Ginkgo](https://ginkgo-project.github.io/)</dt>
    <dd>
        [Ginkgo](https://ginkgo-project.github.io/)
        is a numerical linear algebra library with highly optimized kernels
        for many core architectures with a focus on fine level parallelism.
        It allows for easy switching of the executing paradigm (CUDA, OpenMP, etc.)
        while providing a multitude of linear solvers and preconditioners
        and extension to other linear operators with minimal changes required in the code.
        To enable Ginkgo, pass `-DGINKGO_DIR=/path/to/ginkgo` to CMake when
        configuring deal.II. For more detailed instructions, one can refer to
        [this page](external-libs/ginkgo.html).

    </dd>
    <dt>             [Gmsh](http://gmsh.info/)</dt>
    <dd>
        [Gmsh](http://gmsh.info/)
        is a 3D mesh generator. The executable can be used
        to create meshes from within deal.II by specifying
        the relevant input data. Gmsh should be readily
        packaged by most Linux distributions. To use a
        self compiled version,
        pass `-DGMSH_DIR=/path/to/gmsh` to the
        deal.II CMake call. Note that netgen, tetgen and
        blas support has to be enabled in Gmsh.

    </dd>
    <dt>[GSL](http://www.gnu.org/software/gsl/)</dt>
    <dd>
        The [GNU Scientific Library](http://www.gnu.org/software/gsl/) provides a wide range of mathematical routines such as random number generators, special functions and least-squares fitting.
        [GSL](http://www.gnu.org/software/gsl/) should be readily packaged by most Linux distributions. To use a self compiled version, pass
        `-DGSL_DIR=/path/to/gsl` to the deal.II CMake call.

    </dd>
    <dt>[HDF5](http://www.hdfgroup.org/HDF5/)</dt>
    <dd>
        The [HDF5 library](http://www.hdfgroup.org/HDF5/) provides graphical output capabilities in `HDF5/XDMF` format.
        [HDF5](http://www.hdfgroup.org/HDF5/) should be readily packaged by most Linux distributions. To use a self compiled version, pass
        `-DHDF5_DIR=/path/to/hdf5` to the deal.II CMake call.

    </dd>
    <dt>[METIS](http://glaros.dtc.umn.edu/gkhome/metis/metis/overview)</dt>
    <dd>
        [METIS](http://glaros.dtc.umn.edu/gkhome/metis/metis/overview) is a library that provides various methods to partition graphs. 
        <acronym>deal.II</acronym> uses it in programs like the step-17 tutorial to partition
        a mesh for parallel computing. To use a self compiled version, pass
        `-DMETIS_DIR=/path/to/metis` to the deal.II CMake call.
        <acronym>deal.II</acronym> supports METIS 5 and later.


        **Note:** A more modern way to support parallel computations is shown in the step-40 tutorial program and is based on the `p4est` library instead of METIS. See below on installing `p4est`.

    </dd>
    <dt>	[muparser](http://muparser.beltoforion.de/)</dt>
    <dd>
        [muparser](http://muparser.beltoforion.de/) is a library that allows to enter functions in text form and have them interpreted at run time. This is particularly useful in input parameter files. `cmake` will usually
        find the version of this library that comes bundled with 
        <acronym>deal.II</acronym>, but you can specify `-DMUPARSER_DIR=/path/to/muparser` if desired.

    </dd>
    <dt>             [nanoflann](https://github.com/jlblancoc/nanoflann)</dt>
    <dd>
        [nanoflann](https://github.com/jlblancoc/nanoflann) is a C++11 header-only library for building KD-Trees of datasets with different topologies. In particular, it can be used for operations such as finding the
        vertex or cell closest to a given evaluation point that occur frequently in many applications using unstructured meshes. scale eigenvalue problems.
        [nanoflann](https://github.com/jlblancoc/nanoflann) should be readily packaged by most Linux distributions. To use a self compiled version, pass
        `-DNANOFLANN_DIR=/path/to/nanoflann` to the deal.II CMake call.

    </dd>
    <dt>[NetCDF](http://www.unidata.ucar.edu/software/netcdf/)</dt>
    <dd>
        [NetCDF](http://www.unidata.ucar.edu/software/netcdf/) is a library that provides services for reading and writing mesh data (and many other things). 
        <acronym>deal.II</acronym> can use it to read meshes via one
        of the functions of the `GridIn` class.
        [NetCDF](http://www.unidata.ucar.edu/software/netcdf/) should be readily packaged by most Linux distributions. To use a self compiled version, pass
        `-DNETCDF_DIR=/path/to/netcdf` to `cmake`.
        _The deal.II NetCDF bindings are only compatible with an obsolete version of NetCDF and will be removed in a future release of the library unless newer bindings are contributed._
    </dd>
    <dt>	[OpenCASCADE](http://www.opencascade.org/)</dt>
    <dd>                Open CASCADE Technology is a software development kit for applications dealing with 3D CAD data, freely available in open source. Our internal interface works with the legacy version of OpenCASCADE, which you can download and install from the official
                    website, as well as with the OpenCASCADE Community Edition (OCE, available at
                    https://github.com/tpaviot/oce), which offers a cmake interface for its compilation. Alternatively, you can install one of the many external applications that ship with OpenCASCADE internally
                    (for example
                    [SALOME](http://www.salome-platform.org/), or
                    [FreeCAD](http://www.freecadweb.org/)). Further installation instructions can be found [here](external-libs/opencascade.html).
                </dd>
    <dt>[p4est](http://www.p4est.org/)</dt>
    <dd>
        [p4est](http://www.p4est.org/) is a library that 
        <acronym>deal.II</acronym> uses to distribute very large meshes across multiple processors (think meshes with a billion cells on 10,000 processors). Using and
        installing p4est is discussed [here](external-libs/p4est.html). To use a self compiled version, pass the argument
        `-DP4EST_DIR=/path/to/p4est` to the
        `cmake` command.

    </dd>
    <dt>[PETSc](http://www.mcs.anl.gov/petsc/)</dt>
    <dd>
        [PETSc](http://www.mcs.anl.gov/petsc/) is a library that supports parallel linear algebra and many other things.
        [PETSc](http://www.mcs.anl.gov/petsc/) is already packaged by some Linux distributions and should be found automatically if present. To use a
        self compiled version of PETSc, add `-DPETSC_DIR=/path/to/petsc
        -DPETSC_ARCH=architecture` to the argument list for
        `cmake`. The values for these arguments must be the same as those specified when building PETSc.


        To disable the PETSc interfaces in cases where `cmake` automatically finds it, use `-DDEAL_II_WITH_PETSC=OFF`. More information on configuring and building PETSc can be found [here](external-libs/petsc.html).

    </dd>
    <dt>	[ScaLAPACK](http://www.netlib.org/scalapack/)</dt>
    <dd>
        [scalapack](http://www.netlib.org/scalapack/) is a library of high-performance linear algebra routines for parallel distributed memory machines. ScaLAPACK solves dense and banded linear systems, least squares problems, eigenvalue
        problems, and singular value problems. In order to enable this feature, add
        `-DSCALAPACK_DIR=/path/to/scalapack` to the argument list for
        `cmake`. If ScaLAPACK does not have embedded BLACS, you might need to pass `-DBLACS_DIR=/path/to/blacs` as well.

    </dd>
    <dt>[SLEPc](http://www.grycap.upv.es/slepc/)</dt>
    <dd>
        [SLEPc](http://www.grycap.upv.es/slepc/) is a library for eigenvalue computations that builds on PETSc. Its configuration works just like that for PETSc, except that the variable to set is `SLEPC_DIR`.
        For the interface with SLEPc to work, 
        <acronym>deal.II</acronym>'s PETSc interface must also be configured correctly (see above).


        To disable the SLEPc interfaces in cases where `cmake` automatically finds it, use `-DDEAL_II_WITH_PETSC=OFF`. More information on configuring and building SLEPc can be found [here](external-libs/slepc.html).

    </dd>
    <dt>              [SUNDIALS](https://computation.llnl.gov/projects/sundials)</dt>
    <dd>
        [SUNDIALS](https://computation.llnl.gov/projects/sundials) is a collection of solvers for nonlinear and differential/algebraic equations.
        [SUNDIALS](https://computation.llnl.gov/projects/sundials) should be readily packaged by most Linux distributions. To use a self compiled version,
        specify
        `-DSUNDIALS_DIR=/path/to/sundials` to the deal.II CMake call.

    </dd>
    <dt>                [SymEngine](https://symengine.github.io/)</dt>
    <dd>
        [SymEngine](https://github.com/symengine/symengine/) is a symbolic manipulation package, implementing the building blocks of a computer algebra system (CAS) similar to [SymPy](https://www.sympy.org/en/index.html). In particular, it can be used for symbolic differentiation. For using
        [SymEngine](https://symengine.github.io/) with deal.II, version 0.4 or newer is required. To use a self compiled version, pass
        `-DSYMENGINE_DIR=/path/to/symengine` to the deal.II CMake call.

    </dd>
    <dt>[Threading Building Blocks (TBB)](http://www.threadingbuildingblocks.org/)</dt>
    <dd>
        The [Threading Building Blocks (TBB)](http://www.threadingbuildingblocks.org/) is a library that provides advanced services for using multiple processor cores on a single machine and is used in 
        <acronym>deal.II</acronym>                    to parallelize many operations. If not found in a system-wide location, `cmake` will resort to the version bundled as part of the 
        <acronym>deal.II</acronym> download. It is always enabled unless threads are explicitly disabled,
        see above.

    </dd>
    <dt>[Trilinos](http://trilinos.org)</dt>
    <dd>
        [Trilinos](http://trilinos.org) is a library for
        parallel linear algebra and all sorts of other
        things as well. To interface with a self compiled
        version of [Trilinos](http://trilinos.org)
        add `-DTRILINOS_DIR=/path/to/trilinos`
        to the argument list
        for `cmake`. Alternatively, you can
        also set an environment
        variable `TRILINOS_DIR`
        and `cmake` will pick up this path.


        To disable the Trilinos interfaces in cases where
        `cmake` automatically finds it, use
        `-DDEAL_II_WITH_TRILINOS=OFF`. More details about compatibility and configuration can be found
        [here](external-libs/trilinos.html).

    </dd>
    <dt>[UMFPACK](http://faculty.cse.tamu.edu/davis/suitesparse.html)</dt>
    <dd>
        [UMFPACK](http://faculty.cse.tamu.edu/davis/suitesparse.html), which is part of SuiteSparse, is a sparse direct solver that we often use in prototype codes where the goal is to simply get a linear system solved robustly.
        The interface will be enabled by default, either using a version installed on your system of using a version that comes bundled with
        <acronym>deal.II</acronym>. It can be disabled explicitly by using the
        `-DDEAL_II_WITH_UMFPACK=OFF` argument. To use a self compiled version, pass the argument
        `-DUMFPACK_DIR=/path/to/umfpack` to the
        `cmake` command.


        SuiteSparse has its own license. To use it with
        deal.II, please read it and make sure that you agree
        with it. You can find the license of SuiteSparse inside
        the SuiteSparse download at the link given above. We
        include UMFPACK in the deal.II repository courtesy of
        its author, [Timothy A. Davis](http://faculty.cse.tamu.edu/davis/welcome.html).

    </dd>
</dl>
<dt>              [zlib](http://zlib.net/)</dt>
<dd>
    [zlib](http://zlib.net/) is a software library used for lossless data-compression. It is used in deal.II whenever compressed data is to be written.
    [zlib](http://zlib.net/) should be readily packaged by most Linux distributions. To use a self compiled version, pass
    `-DZLIB_DIR=/path/to/zlib` to the deal.II CMake call.

</dd>    

#### More information on configuring and building the library



The 
<acronym>deal.II</acronym> `cmake` system allows far greater control over what exactly is configured or built than just the outline above. If you want to learn more about this, take a look
[here](users/cmake_dealii.html). You might also be interested in
[CMake for user projects](users/cmake_user.html) or
[build system internals](developers/cmake-internals.html).



License
-------

The deal.II library is free software; you can use it, redistribute it, and/or modify it under the terms of the
[GNU Lesser General
Public License](http://www.gnu.org/licenses/lgpl-2.1.html) (LGPL) as published by the Free Software Foundation; either version 2.1 of the License, or (at your option) any later version.

This allows you to use the library free of charge for private, academic, or commercial use (under the terms of the LGPL v2.1 or later). You are guaranteed full access to the source code and are encouraged to help in the further development of the library.
Follow
[this
link](http://www.dealii.org/license.html) for detailed information.

Please note:

*             Detailed license information can be found following
                [this link](http://www.dealii.org/license.html).

* **As a contributor to this project, you agree that any of your
              contributions be licensed under the same terms and conditions as
              the license of the deal.II project granted to you.**
*             We, [the deal.II Authors](http://www.dealii.org/authors.html), do not require copyright assignments for contributions. This means that the copyright for code contributions in the deal.II project is held by its respective
                contributors who have each agreed to release their contributed code under the terms of the LGPL v2.1 or later.

*             In addition to the terms imposed by the LGPL (version 2.1 or later), we ask for the courtesy that scientific publications presenting results obtained with this libraries acknowledge its use. Please cite one of the papers referenced
                [here](http://www.dealii.org/publications.html).

* <acronym>deal.II</acronym> can interface with a number of other packages that you either have to install yourself. They are, of course, covered by their own licenses. In addition, deal.II comes bundled with
                copies of
                [          UMFPACK](http://faculty.cse.tamu.edu/davis/suitesparse.html),
                [Threading Building Blocks](http://threadingbuildingblocks.org/),
                [BOOST](http://www.boost.org/) and
                [muparser](http://muparser.beltoforion.de/), courtesy of their authors. These are also covered by their own licenses; please refer to their webpages for more information.


---

<div class="right">[      ![Valid HTML 4.01!](http://www.w3.org/Icons/valid-html401)](http://validator.w3.org/check?uri=referer)
        [      ![Valid CSS!](http://jigsaw.w3.org/css-validator/images/vcss)](http://jigsaw.w3.org/css-validator/check/referer)</div>