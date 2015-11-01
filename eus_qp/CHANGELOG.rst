^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package eus_qp
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

0.1.7 (2015-11-01)
------------------
* [3rdparty/eiquadprog.hpp] using std::abs instead of internal::abs
* CMakeLists.txt: using test as execute name may confuse system
* [eus_qp/euslisp/model-predictive-control.l] Support output variables in evaluation
* [eus_qp/euslisp/model-predictive-control.l] Return world input value (wrench)
* [eus_qp/euslisp/contact-optimization.l, model-predictive-control.l, test-model-predictive-control.l] Fix bug of mpc inequality-matrix contact coords and update samples
* [eus_qp/euslisp/*model-predictive-control.l, test/test_model_predictive_control.*, CMakeLists.txt] Add model predictive control from Nagasaka'2012 and add examples and tests.
* [eus_qp/euslisp/contact-optimization.l, eus_qp/euslisp/test-contact-wrench-opt.l] Add no-contact constraint and tests
* [../../eus_qp/euslisp/contact-optimization.l,test-eus-qpoases.l,eus-qpoases.l] Rename solve-qpoases => solve-qpoases-qp and remain solve-qpoases for backward compatibility with warning.
* Remove manifest.xml and Makefile and use catkin style filesystem
* Rename samplerobot demo function add infeasible sample. Add to rostest.
* Do not use immediate value for max demo function num
* Add test for force min violation
* Add inequality constraint violation mode if user set min-inequality-violation-weight.
* add sample for testing sliding contact constraint
* add translational sliding constraint to contact-optimization.l
* Add min-max constraint
* Use contact-constraint-vector-list
* Update test for test-contact-wrench-opt.l
* Add demo programe for all contact constraints
* Rename friction contact constraint
* Add constraint vector and use constraint-matrix slots variable
* Fix order of drawing
* Fix force color
* Add test for wrench contact application
* Add contact optimization application using euslisp qp calculation
* Contributors: Kei Okada, Ryohei Ueda, Shunichi Nozawa, Masaki Murooka

0.1.6 (2015-06-11)
------------------
* [eus_qp] Fix for indigo. Eigen3 on indigo may not provide Eigen::internal::sqrt
  Eigen::internal::abs, in order to provide them, we define these function in qp_lib.cpp
  before including qp stuff.

0.1.5 (2015-01-08)
------------------

0.1.4 (2014-10-21)
------------------
* add eigen to depend

0.1.3 (2014-10-10)
------------------

0.1.2 (2014-09-08)
------------------
* eigen is no longer ros package
* add catkin_package()
* Contributors: Kei Okada

0.1.1 (2014-09-04)
------------------
* use find_package(catkin COMPONENTS cmake_modules)
* add dependancies of euslisp and eigen
* bag fix load-library functions
* fix eiquadprog.l, plugin load from LD_LIBRARY_PATH
* add package.xml,
* add solve-eiquadprog-raw-with-error function, solve qp with error tolerance, usage=solve-eiquadprog :eiquadprog-function 'solve-eiquadprog-raw-with-error,
* bug fix of check_constraints function, args order change
* eq constraints check fix, but this is unbeliabable mistake, why it could be move?
* returns nil if eiquadprog is not solved
* fix args for qp_lib.cpp change
* add some comment, and constrants check result set in global value flag
* add constraints check functions
* remove unused comment
* fix debug mode stop the main functino
* rename state variable name from f0
* rename eq -> equality , non-eq -> inequality
* fix typo ;; min->max
* .l bug fix, eq constraints mean CEx + ce = 0
* fix test function, plus minus changed
* add Makefile
* add eus_qp dir, solve qp problem with euslisp, use eigenquadprog library
* Contributors: Shintaro Noda, Shunichi Nozawa
