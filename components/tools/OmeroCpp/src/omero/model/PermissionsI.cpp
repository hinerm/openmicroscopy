/*
 *   $Id$
 *
 *   Copyright 2007 Glencoe Software, Inc. All rights reserved.
 *   Use is subject to license terms supplied in LICENSE.txt
 *
 */

#include <omero/model/PermissionsI.h>
#include <omero/ClientErrors.h>

namespace omero {

    namespace model {

	PermissionsI::~PermissionsI() {}
	PermissionsI::PermissionsI(const std::string& perms) : Permissions() {
            if (perms.empty()) {
                perm1 = -1L;
            } else {
                // Due to lack of regex libraries
                // this implementation is more naive
                // than in the other SDKs
                std::string rest = perms;
                if (rest.size() == 7) {
                    // ignore the locked character
                    rest = rest.substr(1);
                }
                if (rest.size() != 6) {
                    std::string msg = "Bad permissions:";
                    msg += perms;
                    throw omero::ClientError(__FILE__, __LINE__, msg.c_str());
                }
                if (rest[0] == 'r' || rest[0] == 'R') {
                    setUserRead(true);
                }
                if (rest[1] == 'w' || rest[1] == 'W') {
                    setUserWrite(true);
                }
                if (rest[2] == 'r' || rest[2] == 'R') {
                    setGroupRead(true);
                }
                if (rest[3] == 'w' || rest[3] == 'W') {
                    setGroupWrite(true);
                }
                if (rest[4] == 'r' || rest[4] == 'R') {
                    setWorldRead(true);
                }
                if (rest[5] == 'w' || rest[5] == 'W') {
                    setWorldWrite(true);
                }
            }
	}

	// shift 8; mask 4
	bool PermissionsI::isUserRead(const Ice::Current& c) {
	    return granted(4,8);
	}
	void PermissionsI::setUserRead(bool value, const Ice::Current& c) {
	    set(4,8, value);
	}

	// shift 8; mask 2
	bool PermissionsI::isUserWrite(const Ice::Current& c) {
	    return granted(2,8);
	}
	void PermissionsI::setUserWrite(bool value, const Ice::Current& c) {
	    set(2,8, value);
	}

	// shift 4; mask 4
	bool PermissionsI::isGroupRead(const Ice::Current& c) {
	    return granted(4,4);
	}
	void PermissionsI::setGroupRead(bool value, const Ice::Current& c) {
	    set(4,4, value);
	}

	// shift 4; mask 2
	bool PermissionsI::isGroupWrite(const Ice::Current& c) {
	    return granted(2,4);
	}
	void PermissionsI::setGroupWrite(bool value, const Ice::Current& c) {
	    set(2,4, value);
	}

	// shift 0; mask 4
	bool PermissionsI::isWorldRead(const Ice::Current& c) {
	    return granted(4,0);
	}
	void PermissionsI::setWorldRead(bool value, const Ice::Current& c) {
	    set(4,0, value);
	}

	// shift 0; mask 2
	bool PermissionsI::isWorldWrite(const Ice::Current& c) {
	    return granted(2,0);
	}
	void PermissionsI::setWorldWrite(bool value, const Ice::Current& c) {
	    set(2,0, value);
	}

	bool PermissionsI::granted(int mask, int shift) {
	    return (perm1 & (mask<<shift) ) == (mask<<shift);
	}

	void PermissionsI::set(int mask, int shift, bool on) {
	    if (on) {
		perm1 = perm1 | ( 0L  | (mask<<shift) );
	    } else {
		perm1 = perm1 & ( -1L ^ (mask<<shift) );
	    }
	}

    }
} //End omero::model
