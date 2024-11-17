const assert = require('assert');
const calculateNumber = require('./1-calcul.js');

    describe('Test the calculateNumber sum, subtract and divide', function() {

        it('should returnthe SUM OF ROUNDED NUMBER', function() {
            assert.strictEqual(calculateNumber('sum', 1.4, 4.5), 6);
        });
    
        it('should return the Difference between a & b', function() {
            assert.strictEqual(calculateNumber('sub', 1.4, 4.5), -4);
        });
    
        it('should return the Division of a & b', function() {
            assert.strictEqual(calculateNumber('division', 1.4, 4.5), 0.2);
        });
    
        it('should return the Division by 0 shld throw error', function() {
            assert.strictEqual(calculateNumber('division', 1.4, 0), 'Error');
        });
});
