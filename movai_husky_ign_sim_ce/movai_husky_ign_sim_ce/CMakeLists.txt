cmake_minimum_required(VERSION 3.0.2)
project(movai_husky_ign_sim_ce)

#############
## Install ##
#############
# Installation

set (PACKAGE_DESTINATION ${CMAKE_INSTALL_PREFIX}/share/${PROJECT_NAME}_metadata)

install(DIRECTORY ../metadata
        DESTINATION ${PACKAGE_DESTINATION}
        )

install(FILES ../manifest.txt
        DESTINATION ${PACKAGE_DESTINATION}
)
