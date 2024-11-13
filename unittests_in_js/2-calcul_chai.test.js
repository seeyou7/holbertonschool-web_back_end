import { expect } from 'chai';
import calculateNumber from './2-calcul_chai.js';

    describe('Test the calculateNumber sum, subtract and divide', function() {

        it('should returnthe SUM OF ROUNDED NUMBER', function() {
            expect(calculateNumber('sum', 1.4, 4.5)).to.equal(6);
        });
    
        it('should return the Difference between a & b', function() {
            expect(calculateNumber('sub', 1.4, 4.5)).to.equal(-4);
        });
    
        it('should return the Division of a & b', function() {
            expect(calculateNumber('division', 1.4, 4.5)).to.equal(0.2);
        });
    
        it('should return the Division by 0 shld throw error', function() {
            expect(calculateNumber('division', 1.4, 0)).to.equal('Error');
        });
});
